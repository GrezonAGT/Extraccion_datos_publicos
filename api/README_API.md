# Sobre La API

Este proyecto se construye con FastAPI, donde se realiza una API con el fin de posteriormente acceder a ella localmente
- La API lista todos los registros en: http://127.0.0.1:8000/resources
- Se puede consultar por id en la API
- Se puede filtrar por fecha o palabra clave en el titulo.

## Requisitos previos

Antes de ejecutar instale lo siguiente si no lo tiene:

- pip install uvicorn fastapi psycopg2

## Fuente de datos
Los datos utilizado en esta API se pueden encontrar en: [https://www.datos.gov.co/resource/6hgx-q9pi.json](https://www.datos.gov.co/resource/6hgx-q9pi.json) 

## Implementacion de IA
Para terminar este proyecto se utilizo IA copilot para partes en especifico, en este caso:
- Para realizar la opcion de tener las 2 caracteristicas para filtrar por fecha o por palabra clave y su implementacion en el Query requerido.
- Para permitir a "http://localhost:3000" (frontend) acceder a la API localmente agregando una libreria y un metodo.

## Imagenes proyecto finalizado

<img width="1920" height="1040" alt="image" src="https://github.com/user-attachments/assets/c9d72f3f-5de8-407c-9031-c291d1fdf686" />

## En la ruta de todos los datos
<img width="1920" height="1039" alt="image" src="https://github.com/user-attachments/assets/af8c5f4f-869c-4329-8bd4-410e975871d6" />

## Conclusion
Este proyecto me ayudo a comprender muy bien el funcionamiento de las API, llenando vacios que tenia respecto a su organizacion.
