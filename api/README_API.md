# Sobre La API

Este proyecto es una aplicación en **React** que consume datos de [datos.gov.co](https://www.datos.gov.co/) y muestra en una tabla los proyectos de investigación e innovación aprobados desde el año 2009. 

Permite **buscar proyectos por palabra clave** y ver **detalles** al hacer click en cada fila.

## Requisitos previos

Antes de ejecutar instale lo siguiente si no lo tiene:

- [Node.js](https://nodejs.org/) 
- npx create-react-app frontend  <- Creacion del proyecto
- pip install npm

## Fuente de datos
La API publica utilizada se puede encontrar en: [https://www.datos.gov.co/resource/6hgx-q9pi.json](https://www.datos.gov.co/resource/6hgx-q9pi.json) 

## Implementacion de IA
Para terminar este proyecto se utilizo IA copilot para partes en especifico, en este caso:
- Para la creacion del menu desplegable de los detalles completos
- La implementacion de la barra de busqueda "SearchBar" para encontrar los registros por palabra clave.
- Para la conversion de fechas de norma ISO 8601 a YYYY-MM-DD para mejor visualización.

## Imagenes proyecto finalizado

<img width="1920" height="1040" alt="image" src="https://github.com/user-attachments/assets/1cab695d-543d-4284-8d47-2578398ca3dd" />

### Uso de barra de busqueda
<img width="1920" height="1039" alt="image" src="https://github.com/user-attachments/assets/9bd7278f-5229-4bd2-84fd-eb53ac5070de" />

### Despliegue de detalles
<img width="1920" height="1038" alt="image" src="https://github.com/user-attachments/assets/4e7d9a6a-ab0d-4ce5-aad5-9a4656ea4ec9" />

## Conclusion
Este proyecto fue una experiencia muy enriquecedora. Aunque ya había utilizado React previamente para construir frontends, en esta ocasión pude reforzar de manera práctica muchos conceptos de programación en JavaScript con React. Además, aprendí a manejar de forma más sólida la conexión y consumo de datos desde APIs, lo cual me permitió comprender mejor el flujo de información entre el frontend y los servicios externos.
