from app_registro import app
from flask import render_template,request,redirect
import csv
from datetime import datetime,date

@app.route("/")
def index():
    #llama al archivo
    fichero = open("data/movimientos.csv","r")
    #accede a cada registro de arhivo y lo formatea
    csvReader = csv.reader(fichero,delimiter=",",quotechar='"')
    #creo un array datos vacio para cargar los registros del archivo
    datos=[]
    #recorrer el objeto csvReader y cargar cada registro al array datos
    for item in csvReader:
        datos.append(item)
    return render_template("index.html",pageTitle="Listas",lista=datos)


@app.route("/new",methods=["GET","POST"])
def create():
    if request.method == "GET":#esto puede ser POST o GET
        return render_template("new.html",pageTitle="Alta",typeAction="Alta",typeButon="Guardar")   
    else:
        #acceder al archivo y configurarlo para cargar un nuevo registro
        mifichero =  open('data/movimientos.csv','a',newline='')
        #llamamos al metodo writer de escritura y cargamos el formeto para csv
        lectura= csv.writer(mifichero, delimiter=',',quotechar='"')
        
        #realizar el control de fecha
        date_object = datetime.strptime(request.form['date'], '%Y-%M-%d').date()

        #-dar fomato final de fechas
        #-validar que el request.form.date <= la fecha de hoy
        #-si date > hoy devolver un formulario vacio get de new.html


        if date_object < date.today():
            print("fecha correcta")
        else:
            print("fecha incorrecta")
        
        #registramos los datos recibidos desde el formulario con request.form y lo añadimos con el metodo writerrow
        lectura.writerow([request.form['date'],request.form['concept'],request.form['quantity']])    

        mifichero.close()

    return redirect('/')


        
   
@app.route("/update")
def edit():
    return render_template("update.html",pageTitle="Modificación",typeAction="Modificación",typeButon="Editar") 

@app.route("/delete")
def remove():
    return render_template("delete.html",pageTitle="Eliminar")