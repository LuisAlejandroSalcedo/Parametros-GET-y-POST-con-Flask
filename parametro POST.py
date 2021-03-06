# importamos lo necesario
from flask import Flask, render_template, request

# Instancia de Flask. Aplicación
app = Flask(__name__)

# Creamos nuestro primer route. '/login'
@app.route('/login')
def template():
	# Renderizamos la plantilla. Formulario HTML.
	# templates/form.html
	return render_template("form.html")

# Definimos el route con el método POST
@app.route('/usuario',methods=['POST'])
def usuario():
	# Obtenemos la información del parametro "nombreUser"
	# Esto lo hacemos con el diccionario "form"
	nombreUser = request.form['nombreUser']

	# Retornamos la respuesta
	return "<h1>Bienvenido " + nombreUser + "</h1>"

if __name__ == '__main__':
	# Iniciamos la apicación en modo debug
	app.run(debug=True)
