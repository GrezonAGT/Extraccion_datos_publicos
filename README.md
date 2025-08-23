# Proyecto Técnico – Proyectos de Investigación e innovación

En este repositorio se encuentra cada uno de las partes de la prueba tecnica, llegando hasta el empaquetado en Docker, para su ejecucion recomiendo las siguientes recomendaciones

- Descargar unicamente las carpetas "Contenedor_Docker" y "frontend", ya que en Contenedor_Docker se encuentran los procesos de etl y api integrados y el frontend hace uso de la API local que se genera con el contenedor
- Para revision más a fondo, los codigos utilizados para el proceso ETL y la creacion de la API con Fastapi estan en este mismo repositorio en sus respectivas carpetas, los codigos funcionan de igualmanera localmente.

1. **Extracción y Transformación de Datos**
   - Los datos utilizados se obtuvieron de la fuente: [Proyectos de Investigación e innovación](https://dev.socrata.com/foundry/www.datos.gov.co/fdir-hk5z).
   - Extracción mediante API SODA (datos.gov.co).
   - Normalización de campos clave.
   - Almacenamiento en base de datos local (PostgreSQL).
   
2. **API REST con FastAPI**
   - Endpoints para listar, buscar por ID, filtrar por palabra clave o fecha.

3. **Frontend (React/Vue)**
   - Interfaz sencilla para mostrar registros en tabla.
   - Búsqueda y filtros básicos.
   - Visualización de detalles.

4. **Opcional (Bonus)**
   - Docker Compose para levantar API + DB. 

---
