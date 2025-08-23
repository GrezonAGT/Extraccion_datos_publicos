# Proyecto Técnico – Proyectos de Investigación e innovación

En este repositorio se encuentra cada uno de las partes de la prueba tecnica, llegando hasta el empaquetado en Docker, para su ejecucion recomiendo las siguientes recomendaciones

- Descargar unicamente las carpetas "Contenedor_Docker" y "frontend", ya que en Contenedor_Docker se encuentran los procesos de etl y api integrados y el frontend hace uso de la API local que se genera con el contenedor
- Para revision más a fondo, los codigos utilizados para el proceso ETL y la creacion de la API con Fastapi estan en este mismo repositorio en sus respectivas carpetas, los codigos funcionan de igualmanera localmente.

## Instrucciones de ejecución paso a paso para ejecucion rapida

1. Descargar las carpetas "Contenedor_Docker" y "frontend"
2. Guardar ambas carpetas en un proyecto
3. En la carpeta "Contenedor_Docker" encontrara 2 archivos con el nombre "start", si su sistema operativo es Windows, ejecutar "start.bat", si su sistema opertaivo es Linux o Mac, ejecute "start.sh"
4. Cuando todos los procesos terminen, abra el terminal y situese en la carpeta de frontend previamente descargada y ejecute el comando "npm start"
5. Se le abrira una ventana en el explorardor con una ip local, en esa ventana encontrara el frontend realizado con react conectado a la API.
6. Realice las pruebas de funcionamiento de la ventana, en teoria todo funciona bien.

## Explicación del diseño
Los programas aqui presentes se dividen escencialmente en 3, programa de ETL, programa de la API y programa de frontend. 

### Programa ETL
En el programa de ETL, inicialmente se extraen los datos de una API publica del gobierno nacional de Colombia, especificamente: [Proyectos de Investigación e innovación](https://dev.socrata.com/foundry/www.datos.gov.co/6hgx-q9pi) dichos datos son observados y se determina cuales son los importantes, y que tipo de veriable son (str, date, numeric), con esto en mente se realiza la transformacion, donde se normalizan los registros (se dejan unicamene los 6 mas importantes: Código Proyecto, Título, Fecha Registro, Nombre Programa CTI, Área Temática y Ciudad), a estos datos se les asigna su respectivo tipo de dato, finalmente se realiza la carga de los registros a una base de datos local de nombre "proyectos_investigacion" en PostgreSQL.

### Programa API
El programa API, se realizo con la libreria FastAPI, con la cual se definieron los respectivos Endpoints de nuestra API;
- [http://localhost:8000/](http://localhost:8000/)  <-- Home o raiz de la api
- [http://localhost:8000/resources](http://localhost:8000/resources) <-- Listado de todos los registros
- [http://localhost:8000/resource/{id}](http://localhost:8000/1) <-- Registro obtenido de la busqueda por ID
- [http://localhost:8000/filtrar](http://localhost:8000/filtrar) <-- Resultados de filtrar por fecha o palabra clave en el titulo
Para poder visualizar de mejor manera los filtros se recomienda iniciar en docs y utilizar esa interfaz.
- [http://localhost:8000/docs](http://localhost:8000/docs)

### Programa frontend
El frontend fue desarrollado con React y hace la conexion con la API creada localmente
