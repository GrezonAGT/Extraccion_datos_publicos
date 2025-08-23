# Sobre el empaquetado

Para la ejecución rapida de este empaquetado debe tener en cuenta su sistema operativo

## Windows:
Si su sistema operativo es windows descague la carpeta completa de "Contenedor_Docker" y ejecute el archico "start.bat", una vez lo ejecute ya puede acceder a la API de manera local

## Linux & MAC
Si su sistema operativo es Linux o MAC descargue la carpeta completa de "Contenedor_Docker" y ejecute el archivo "start.sh", una vez lo ejecute ya puede acceder a la API de manera local

Asegurese de dar permisos de ejecución: 
```
chmod +x start.sh
```

## Si NO puede ejecutar el start.bat realice lo siguiente
Si de alguna manera no puede ejecutar el start.bat, descargue la carpeta "Contenedor_Docker", posicionese en ella y ejecute los siguientes comandos en el bash:
docker compose build
docker compose up -d

Con eso ya deberia de poder acceder rapidamente a la API desde [http://localhost:8000/doc](http://localhost:8000/redoc)

## Conclusion
Personalmente, nunca había trabajado con Docker, pero me pareció una herramienta muy interesante y con gran funcionalidad. Al principio me costó comprender su funcionamiento, pero después de
leer documentación, consultar foros y ver algunos videos en YouTube, pude entenderlo mucho mejor. Esta experiencia resultó de gran ayuda para familiarizarme con el empaquetado de aplicaciones.
