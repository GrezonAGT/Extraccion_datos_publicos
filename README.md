# Proyecto Técnico – Tratados Internacionales de Colombia

Este proyecto es una prueba técnica cuyo objetivo es validar mi capacidad para extraer datos públicos, procesarlos, exponerlos mediante una API y construir un frontend sencillo, todo en un entorno local.

1. **Extracción y Transformación de Datos**
   - Fuente: [Tratados Internacionales de Colombia](https://dev.socrata.com/foundry/www.datos.gov.co/fdir-hk5z).
   - Extracción mediante API SODA (datos.gov.co).

   - Normalización de campos clave (título, fecha, estado, país, enlace).
   - Almacenamiento en base de datos local (SQLite).

3. **API REST con FastAPI**
   - Endpoints para listar, buscar por ID, filtrar por palabra clave o fecha.

4. **Frontend (React/Vue)**
   - Interfaz sencilla para mostrar registros en tabla.
   - Búsqueda y filtros básicos.
   - Visualización de detalles.

5. **Opcional (Bonus)**
   - Docker Compose para levantar API + DB.

---
