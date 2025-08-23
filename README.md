# Proyecto Técnico – Proyectos de Investigación e innovación

En este repositorio se encuentra cada una de las partes de la prueba técnica, llegando hasta el empaquetado en Docker, para su ejecución recomiendo las siguientes recomendaciones

- Descargar únicamente las carpetas "Contenedor_Docker" y "frontend", ya que en Contenedor_Docker se encuentran los procesos de etl y api integrados y el frontend hace uso de la API local que se genera con el contenedor
- Para revisión más a fondo, los códigos utilizados para el proceso ETL y la creación de la API con Fastapi están en este mismo repositorio en sus respectivas carpetas, los códigos funcionan de igual manera localmente.

## Instrucciones de ejecución paso a paso para ejecución rápida

1. Descargar las carpetas "Contenedor_Docker" y "frontend"
2. Guardar ambas carpetas en un proyecto
3. En la carpeta "Contenedor_Docker" encontrara 2 archivos con el nombre "start", si su sistema operativo es Windows, ejecutar "start.bat", si su sistema operativo es Linux o Mac, ejecute "start.sh"
4. Cuando todos los procesos terminen, abra el terminal y sitúese en la carpeta de frontend previamente descargada y ejecute el comando "npm start"
5. Se le abrirá una ventana en el explorador con una ip local, en esa ventana encontrara el frontend realizado con react conectado a la API.
6. Realice las pruebas de funcionamiento de la ventana, en teoría todo funciona bien.

## Explicación del diseño
Los programas aquí presentes se dividen esencialmente en 3, programa de ETL, programa de la API y programa de frontend. 

### Programa ETL
En el programa de ETL, inicialmente se extraen los datos de una API publica del gobierno nacional de Colombia, específicamente: [Proyectos de Investigación e innovación](https://dev.socrata.com/foundry/www.datos.gov.co/6hgx-q9pi) dichos datos son observados y se determina cuáles son los importantes, y que tipo de variable son (str, date, numeric), con esto en mente se realiza la transformación, donde se normalizan los registros (se dejan únicamente los 6 más importantes: Código Proyecto, Título, Fecha Registro, Nombre Programa CTI, Área Temática y Ciudad), a estos datos se les asigna su respectivo tipo de dato, finalmente se realiza la carga de los registros a una base de datos local de nombre "proyectos_investigacion" en PostgreSQL.

### Programa API
El programa API, se realizó con la librería FastAPI, con la cual se definieron los respectivos Endpoints de nuestra API;
- [http://localhost:8000/](http://localhost:8000/)  <-- Home o raíz de la api
- [http://localhost:8000/resources](http://localhost:8000/resources) <-- Listado de todos los registros
- [http://localhost:8000/resource/{id}](http://localhost:8000/1) <-- Registro obtenido de la búsqueda por ID
- [http://localhost:8000/filtrar](http://localhost:8000/filtrar) <-- Resultados de filtrar por fecha o palabra clave en el titulo
Para poder visualizar de mejor manera los filtros se recomienda iniciar en docs y utilizar esa interfaz.
- [http://localhost:8000/docs](http://localhost:8000/docs)

### Programa frontend
El frontend fue desarrollado con React y hace la conexión con la API creada localmente, todo se divide en componentes para poder realizar correcciones de mejor forma, este proyecto inicia localmente en;
```
Local:            http://localhost:3000        
On Your Network:  http://192.168.20.18:3000
```
### imágenes de la APP corriendo:
#### Todos los registros:
<img width="1920" height="1037" alt="image" src="https://github.com/user-attachments/assets/67c1231a-21fd-40b7-86d9-38d31bbc7c2f" />

#### Filtrados por nombre:
<img width="1920" height="1038" alt="image" src="https://github.com/user-attachments/assets/77c49ae9-5faf-4bc1-bd98-8a751740b654" />

#### Detalles de un registro:
<img width="1920" height="1039" alt="image" src="https://github.com/user-attachments/assets/cf9f85d8-bcf9-431c-bce9-9c7198e3d708" />

### imágenes de la API corriendo:
<img width="1920" height="1040" alt="image" src="https://github.com/user-attachments/assets/2653aa75-dd90-4cc4-b46d-3a34a4851945" />

#### Con su filtro id: 
<img width="1920" height="1039" alt="image" src="https://github.com/user-attachments/assets/95a2bfe4-8025-4398-9f87-9bc1b7ec7c89" />

#### Con su filtro de fecha y palabra clave en el título:
<img width="1920" height="1039" alt="image" src="https://github.com/user-attachments/assets/fae59528-5785-40b2-88ab-6a2117fc7d56" />

Dentro de cada carpeta de cada código se encuentra un README con las especificaciones del código en cuestión donde se detallan un poco más.

Muchas Gracias

Autor: Andres Garces.
