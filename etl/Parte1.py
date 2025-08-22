import pandas as pd
from sodapy import Socrata
import psycopg2
from psycopg2 import sql
import numpy as np

"""
Codigo para conectarse a la API de datos abiertos https://dev.socrata.com/foundry/www.datos.gov.co/6hgx-q9pi.
condigo de extracción suministrado por la documentacion oficial de Socrata.
"""
#Extraccion de datos
client = Socrata("www.datos.gov.co", None)
results = client.get("6hgx-q9pi", limit=2000)
results_df = pd.DataFrame.from_records(results)

#Transformacion de datos
def transformacion(dataframe):
    # Seleccionamos columnas utiles
    datos_normalizados = dataframe[[
        "codigo_proyecto",
        "titulo_proyecto",
        "fecha_registro",
        "nme_prog_cti",
        "area_tematica",
        "nme_ciudad_pry"
    ]].copy()
    
    #Se transforman estos datos de texto a su respectiva variable
    datos_normalizados["codigo_proyecto"] =  pd.to_numeric(datos_normalizados["codigo_proyecto"], errors="coerce")
    datos_normalizados["fecha_registro"] = pd.to_datetime(datos_normalizados["fecha_registro"], errors="coerce")

    datos_normalizados = datos_normalizados.replace({np.nan: None, pd.NaT: None})

    return datos_normalizados

#Carga de datos
def carga(dataframe):
    DB_Datos = {
        "database": "postgres",
        "user": "postgres",
        "password": "andresgarces",
        "host": "localhost",
        "port": 5432
    }

    try:
        conn = psycopg2.connect(**DB_Datos)
        cursor = conn.cursor()
        
        # Crear tabla si no existe
        create_table_query = """
        CREATE TABLE IF NOT EXISTS proyectos_investigacion (
            id SERIAL PRIMARY KEY,
            codigo_proyecto NUMERIC,
            titulo_proyecto TEXT,
            fecha_registro DATE,
            nme_prog_cti TEXT,
            area_tematica TEXT,
            nme_ciudad_pry TEXT
        );
        """
        cursor.execute(create_table_query)
        conn.commit()

        # Insertar datos a la tabla
        if dataframe.empty:
            print("No hay datos para cargar.")
            return
        else:
            for _,row in dataframe.iterrows():
                cursor.execute(
                    sql.SQL("""
                        INSERT INTO proyectos_investigacion (codigo_proyecto, titulo_proyecto, fecha_registro, nme_prog_cti, area_tematica, nme_ciudad_pry)
                        VALUES (%s, %s, %s, %s, %s, %s)
                    """),
                    (
                        row["codigo_proyecto"],
                        row["titulo_proyecto"],
                        row["fecha_registro"],
                        row["nme_prog_cti"],
                        row["area_tematica"],
                        row["nme_ciudad_pry"]
                    )
                )
                conn.commit()
        print("Datos Cargados correctamente.")
    except Exception as e:
        print(f"Error al cargar los datos: {e}")

    finally:
        cursor.close()
        conn.close()
    
# Proceso ETL
Datos_transformados = transformacion(results_df)
if Datos_transformados is not None:
    print("Datos transformados correctamente.")
    carga(Datos_transformados)
else:
    print("No se pudieron transformar los datos.")
