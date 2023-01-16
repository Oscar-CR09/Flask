from flask import Flask, request, render_template, url_for, session
from werkzeug.exceptions import abort
from werkzeug.utils import redirect
from flask import jsonify
app = Flask(__name__)
app.secret_key = 'Mi_llave_secreta'

#http://localhost:5000/
@app.route('/')
def inicio():
    if 'username' in session:
        return f'usuario ya hecho loggin {session["username"]} '
    return  'no a hecho loggin'
  #  app.logger.warn(f'Entramos al path {request.path}')
    #return 'Hola mundo desde Flask.'

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        #omitimos la validadcion de usuario y password
        usuario = request.form['username']
        #agregar el usuario a la secion
        session['username'] = usuario
        #session['username'] = request.form['username']
        return redirect(url_for('inicio'))

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('inicio'))

@app.route('/saludar/<nombre>')
def saludar(nombre):
    return  f'saludos {nombre}'


@app.route('/edad/<int:edad>')
def mostrar_edad(edad):
    return f'Tu edad es: {edad +1 }'

@app.route('/mostrar/<nombre>', methods=['GET','POST'])
def mostrar_nombre(nombre):
    return render_template('mostrar.html', nombre=nombre)

@app.route('/redireccionar')
def redireccionar():
    return redirect(url_for('mostrar_nombre',nombre='Juan'))

@app.route('/salir')
def salir():
    return abort(404)

@app.errorhandler(404)
def pagina_no_encontrada(error):
    return render_template('error404.html',error=error),404

#rest representational state trasnsfer
@app.route('/api/mostrar/<nombre>',methods=['GET','POST'])
def mostrar_json(nombre):
    valores = {'nombre':nombre,'metodo_http':request.method }
    return jsonify(valores)
