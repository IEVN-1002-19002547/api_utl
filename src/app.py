from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

# Decorador. Indica la ruta donde se visualiza el contenido o vista
@app.route('/') 
#Funcion
def index():
    grupo = "IEVN 1002"
    lista = ["IEVN 1001", "IEVN 1002", "IEVN 1003"]
    return render_template('index.html', grupo = grupo, lista = lista)

@app.route('/alumnos')
def alumnos():
    return render_template('alumnos.html')

@app.route('/hola')
def hola():
    return "Saludo UTL"

#Decorador para ruta que pasa el parametro nombre de tipo string
@app.route('/user/<string:nombre>')
#Funcion para ruta que pasa parametro nombre de tipo string
def user(nombre):
    return 'Saludo {0}'.format(nombre)

#Decorador para ruta que pasa el parametro numero 1 de tipo int
@app.route('/numero/<int:n1>')
#Funcion para ruta que pasa parametro numero 1 de tipo int
def numero(n1):
    return 'El numero es: {}'.format(n1)

#Decorador para ruta que pasa dos parametros, el ID de tipo int y el NOMBRE de tipo string
@app.route('/user/<int:id>/<string:nom>')
#Funcion para ruta que pasa parametro ID de tipo int y el NOMBRE de tipo string
def userUno(id, nom):
    return 'ID: {} NOMBRE: {}'.format(id, nom)

#Decorador para ruta que pasa dos parametros de tipo float:  n1 (numero 1) y n2 (numero 2) y los suma
@app.route('/suma/<float:n1>/<float:n2>')
#Funcion para ruta que pasa dos parametros de tipo float:  n1 (numero 1) y n2 (numero 2) y los suma
def suma(n1, n2):
    return 'La suma es: {}'.format(n1 + n2)

#Decorador para ruta default que no pasa parametros
@app.route('/default')
#Decorador para ruta default que pasa parametro de tipo string dd
@app.route('/default/<string:dd>')
#Funcion para ruta default que pasa parametro de tipo string dd con formato
def defautl(dd = 'fulanito'):
    return "<h1>El nombre es: {} </h1>".format(dd)



if __name__ == "__main__":
    app.run(debug=True) #Debug con valor true permite visualizar cambios al guardar el codigo