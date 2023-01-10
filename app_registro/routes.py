from app_registro import app
from flask import render_template
from datetime import datetime, date
import requests

@app.route('/')
def index():

    import csv

    datos = []
    # 'Seleccionamos' el archivo a leer
    fichero = open('data/movimientos.txt', 'r')
    # Crear variable CSV que formatee los datos de movimientos.txt
    csvreader = csv.reader(fichero, delimiter=",", quotechar='"')
    # Extraer los datos formateados por CSV
    for registro in csvreader:
        #Guardarlos en una variable con el nuevo formato
        datos.append(registro)

    fichero.close()

    return render_template('index.html', pageTitle='Página Principal', lista=datos)

# Se agrega GET y POST para que Flask sepa que esta ruta puede recibir el protocolo de comunicación de unos de éstos métodos.
@app.route('/new', methods=["GET", "POST"])
def new():
    if requests.method == "GET": # Puede ser POST o GET
        return render_template("new_register.html", pageTitle="Nuevo registro", typeAction="Agregar", typeButon="Guardar", dataForm={})
    else:
        # El modo 'a' es para añadir datos, significa 'append'
        fichero = open('data/movimientos.csv', 'a', newline="")

    return render_template('new_register.html', pageTitle='Nuevo registro', typeButton='Agregar', typeAction='agregar')

@app.route('/base')
def base():
    return render_template('base.html', pageTitle='Página Base')

@app.route('/update')
def update():
    return render_template('update_register.html', pageTitle='Actualizar registro', typeButton='Modificar', typeAction='modificar')

@app.route('/delete')
def delete():
    return render_template('delete_register.html', pageTitle='Eliminar registro', typeButton='Eliminar')

@app.route('/form')
def form():
    return render_template('form.html', pageTitle='Formulario base')