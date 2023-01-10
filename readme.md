# Aplicación Web Ingresos-Gastos

Programa hecho en Python con el framework Flask, App Ingresos-Gastos


## En su entorno de Python, ejecutar el siguiente comando:

    pip install -r requirements.txt


Flask https://flask.palletsprojects.com/en/2.2.x/


## Ejecución del programa

- Inicializar el servidor de Flask, ejecutando los siguientes comandos:

    En macOS/Linux:

        export FLASK_APP=main.py

    En Microsoft Windows:

        set FLASK_APP=main.py

- Para ejecutar el servidor, usar el comando siguiente:

        flask --app main run


## Comando para actualizar el servidor con cambios de código en tiempo real

    flask --app main --debug run

## -  Alternativamente, para no tener que ejecutar cada vez el comando anterior, crea un archivo .env (oculto), con los siguientes datos:

        FLASK_APP=main.py
        DEBUG=True

## Comando para ejecutar el servidor en un puerto 

Utilizarse en caso de que el puerto 5000 no esté disponible

    flask --app main run -p 5001

## Comando para lanzar en modo debug y con puerto específico

    flask --app main --debug -p 5001