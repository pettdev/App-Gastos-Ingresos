from flask import Flask

app = Flask(__name__)


#hago referencia a todas las rutas
#definidas dentro de routes.py
from app_registro.routes import *

#inicializar el servidor de flask
# en mac: export FLASK_APP=main.py
# en windows: set FLASK_APP=main.py
# o otra alternativa seria crear el archivo oculto .env y dentro agregar las siguientes lineas
#FLASK_APP=main.py
#FLASK_DEBUG=true

# flask --app main --debug run