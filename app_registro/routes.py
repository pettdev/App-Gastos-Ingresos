from app_registro import app
from flask import render_template

@app.route('/')
def index():

    datos = [
        {
            'Fecha': '18/12/2022',
            'Concepto': 'Regalo de Reyes',
            'Cantidad': '-275.50'
        },

        {   'Fecha': '19/12/2022',
            'Concepto': 'Cobro de trabajo',
            'Cantidad': '1200.00'
        },

        {   'Fecha': '18/12/2022',
            'Concepto': 'Ropa de Navidad',
            'Cantidad': '-355.50'
        }
    ]

    return render_template('index.html', pageTitle='Página Principal', lista=datos)

@app.route('/new')
def new():
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