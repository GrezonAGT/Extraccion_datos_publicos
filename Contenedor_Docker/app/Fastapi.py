from fastapi import FastAPI, HTTPException, Query
import psycopg2
from datetime import datetime
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os

#Creamos la instancia de FastAPI
app = FastAPI(title="API de Proyectos de Investigación", version="1.0")

#Definimos los endpoints
#Endpoint raiz
@app.get("/", summary="Verificar que la API está funcionando")
def raiz():
    return {"mensaje": "API de Proyectos de Investigación está funcionando"}

#Endpoint para listar todos los registros
@app.get("/resources", summary="Listado de todos los registros")
def listado_completo():
    DB_Datos = {
        "database": os.getenv("DB_NAME", "postgres"),
        "user": os.getenv("DB_USER", "postgres"),
        "password": os.getenv("DB_PASS", "andresgarces"),
        "host": os.getenv("DB_HOST", "localhost"),
        "port": int(os.getenv("DB_PORT", 5432)),
    }

    try:
        conn = psycopg2.connect(**DB_Datos)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM proyectos_investigacion;")
        records = cursor.fetchall()
        columnas = [desc[0] for desc in cursor.description] # Obtener nombres de columnas
        resultados = [dict(zip(columnas, row)) for row in records]
        return resultados
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al conectar a la base de datos: {e}")
    finally:
        if conn:
            cursor.close()
            conn.close()

#Endpoint para obtener un registro por ID
@app.get("/resource/{id}", summary="Obtener un registro por ID")
def obtener_por_id(id: int):
    DB_Datos = {
        "database": os.getenv("DB_NAME", "postgres"),
        "user": os.getenv("DB_USER", "postgres"),
        "password": os.getenv("DB_PASS", "andresgarces"),
        "host": os.getenv("DB_HOST", "localhost"),
        "port": int(os.getenv("DB_PORT", 5432)),
    }
    try:
        conn = psycopg2.connect(**DB_Datos)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM proyectos_investigacion WHERE id = %s;", (id,))
        record = cursor.fetchone()
        if record:
            columnas = [desc[0] for desc in cursor.description] # Obtener nombres de columnas
            resultado = dict(zip(columnas, record))
            return resultado
        else:
            raise HTTPException(status_code=404, detail="Registro no encontrado")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al conectar a la base de datos: {e}")
    finally:
        if conn:
            cursor.close()
            conn.close()

#Endpoint para filtrar por fecha o por palabra clave en el título
@app.get("/filtrar", summary="Filtrar por fecha o por palabra clave en el título.")
def filtrar(fecha: Optional[str] = Query(None, description="Fecha en formato YYYY-MM-DD"),
            palabra_clave: Optional[str] = Query(None, description="Palabra clave en el título")):
    DB_Datos = {
        "database": os.getenv("DB_NAME", "postgres"),
        "user": os.getenv("DB_USER", "postgres"),
        "password": os.getenv("DB_PASS", "andresgarces"),
        "host": os.getenv("DB_HOST", "localhost"),
        "port": int(os.getenv("DB_PORT", 5432)),
    }
    try:
        conn = psycopg2.connect(**DB_Datos)
        cursor = conn.cursor()
        
        query = "SELECT * FROM proyectos_investigacion WHERE TRUE"
        params = []
        
        if fecha:
            query += " AND fecha_registro >= %s"
            params.append(datetime.strptime(fecha, "%Y-%m-%d").date())
        
        if palabra_clave:
            query += " AND titulo_proyecto ILIKE %s"
            params.append(f"%{palabra_clave}%")

        if not params:
            raise HTTPException(status_code=404, detail="No se encuentran registros con los filtros aplicados.")
        
        cursor.execute(query, params)
        records = cursor.fetchall()
        columnas = [desc[0] for desc in cursor.description] # Obtener nombres de columnas
        resultados = [dict(zip(columnas, row)) for row in records]
        
        return resultados
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al conectar a la base de datos: {e}")
    finally:
        if conn:
            cursor.close()
            conn.close()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # o ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)