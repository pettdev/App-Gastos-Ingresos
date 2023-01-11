#lectura de archivos
#with open('data/movimientos.csv',"r") as resultado:
#    leer = resultado.read()
#    print(type(leer))

#otra manera
#result = open("data/movimientos.csv","r")
#lectura = result.readlines()
#print(type(lectura))
import csv
'''
datos = []
mifichero= open("data/movimientos.csv","r")
mifichero = csv.reader(mifichero,delimiter=",",quotechar='"')

for registros in mifichero:
    print(registros)
    datos.append(registros)

print("esto es datos:",datos)
'''

'''
mifichero =  open('data/movimientos.csv','a',newline='')
lectura= csv.writer(mifichero, delimiter=',',quotechar='"')
lectura.writerow(['19/12/2022','Compra de arbol de navidad',-100.50])    

mifichero.close()
'''

from datetime import datetime,date

date_str = '09-19-2022'

date_object = datetime.strptime(date_str, '%m-%d-%Y').date()
print(type(date_object))
print(date_object)  # printed in default format

print("fechalocal",date.today())
print("fechalocal",type(date.today()))