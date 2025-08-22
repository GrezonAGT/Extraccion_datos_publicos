import requests
from datetime import datetime
import psycopg2
from psycopg2 import sql

# URL de la API:
URL = "https://www.datos.gov.co/resource/fdir-hk5z.json"

# Base de datos PostgreSQL:
database_1 =  'postgres'
host_1 = 'localhost'
user_1 = 'postgres'
password_1 = 'andresgarces'
port_1 = 5432

# EXTRACCION DE DATOS
def extraccion():
    """
    Función encargada de extraer los datos de la API y devolverlos en formato JSON.
    Realiza una petición GET a la URL especificada y devuelve los datos en formato JSON.
    Si la petición falla, imprime un mensaje de error y devuelve None.
    """
    try:
        respuesta = requests.get(URL)
        if not (200 <= respuesta.status_code < 300):
            print(f" Error: {respuesta.status_code}")
            return None
        return respuesta.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

# TRANSFORMACION DE DATOS
def transformacion(Data):
    """
    Función encargada de transformar los datos extraídos.
    Se normalizan los campos de fecha y se seleccionan los campos relevantes.
    Devuelve una lista de diccionarios con los datos normalizados.
    """
    datos_normalizados = []
    """
    Se aclara que se especifica hasta 220 registros, ya que la API en algunos casos 
    devuelve valores que requieren de una transformación especial por una mala carga de datos.
    Vease el registro 224 como ejemplo de error de carga.
    """
    for i in range(220):
        if Data[i].get("fechaadopcion") is not None:
            try:
                Data[i]["fechaadopcion"] = datetime.strptime(Data[i]["fechaadopcion"], "%d/%m/%Y").date()
            except ValueError as e:
                print(f"Error al convertir fecha en registro {i+1}: {e}")
                Data[i]["fechaadopcion"] = None

        Data[i]["vigente"] = True if Data[i].get("vigente") == "SI" else False
        datos_normalizados.append({
            "nombretratado": Data[i].get("nombretratado"),
            "bilateral": Data[i].get("bilateral"),
            "lugaradopcion": Data[i].get("lugaradopcion"),
            "fechaadopcion": Data[i]["fechaadopcion"],
            "temas": Data[i].get("temas"),
            "naturalezatratado": Data[i].get("naturalezatratado"),
            "vigente": Data[i]["vigente"],
        })
    return datos_normalizados

# CARGA DE DATOS
def carga(Data):
    """
    Función encargada de cargar los datos transformados.
    Los datos se subiran a una base de datos local del tipo postgresql.
    """
    # Conexión a la base de datos PostgreSQL
    conn = psycopg2.connect(database = database_1, 
                        user = user_1, 
                        host= host_1,
                        password = password_1,
                        port = port_1)
    cursor = conn.cursor()

    try:
        # Crear la tabla si no existe
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Tratados_internacionales (
                id SERIAL PRIMARY KEY,
                nombretratado TEXT,
                bilateral TEXT,
                lugaradopcion TEXT,
                fechaadopcion DATE,
                temas TEXT,
                naturalezatratado TEXT,
                vigente BOOLEAN)"""
        )
        conn.commit()

        # Limpiar la tabla antes de insertar nuevos datos
        cursor.execute("TRUNCATE TABLE Tratados_internacionales RESTART IDENTITY;")
        conn.commit()

        # Insertar los datos en la tabla
        if not Data:
            print("No hay datos para cargar.")
            return
        for dato in Data:
            cursor.execute(sql.SQL("""
                INSERT INTO Tratados_internacionales (nombretratado, bilateral, lugaradopcion, fechaadopcion, temas, naturalezatratado, vigente)
                VALUES (%s, %s, %s, %s, %s, %s, %s)"""), 
                (dato["nombretratado"],
                dato["bilateral"],
                dato["lugaradopcion"],
                dato["fechaadopcion"],
                dato["temas"],
                dato["naturalezatratado"],
                dato["vigente"])
            )
        conn.commit()
        print("Datos cargados correctamente.")
    except Exception as e:
        print(f"Error al cargar los datos: {e}")
    finally:
        cursor.close()
        conn.close()

#Proceso ETL
Data = extraccion()
if Data is not None:
    print("Datos extraidos correctamente.")
else:
    print("No se pudieron extraer los datos o la base de datos esta vacia.")

Datos_transformados = transformacion(Data)
if Datos_transformados:
    print("Datos transformados correctamente.")
else:
    print("No se pudieron transformar los datos.")

carga(Datos_transformados)
print("Datos cargados, proceso de ETL completado.")
