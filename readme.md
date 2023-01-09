# Aplicación Web Ingresos-Gastos

Programa hecho en Python con el framework Flask, App Ingresos-Gastos


## En su entorno de Python, ejecutar el siguiente comando:

    pip install -r requirements.txt


Flask https://flask.palletsprojects.com/en/2.2.x/


## Ejecución del programa

- Inicializar el servidor de Flask, ejecutando los siguientes comandos:

    En macOS/Linux:

        export FLASK_APP=hello.py

    En Microsoft Windows:

        set FLASK_APP=hello.py

- Para ejecutar el servidor, usar el comando siguiente:

        flask --app hello run


## Comando para actualizar el servidor con cambios de código en tiempo real

    flask --app hello --debug run

## Comando para ejecutar el servidor en un puerto 

Utilizarse en caso de que el puerto 5000 no esté disponible

    flask --app hello run -p 5001

## Comando para lanzar en modo debug y con puerto específico

    flask --app hello --debug -p 5001