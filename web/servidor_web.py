from flask import Flask, request, redirect, url_for
from flask import render_template
from web.servicios import aut, producto

app = Flask(__name__)



@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if not autenticacion.validar_credenciales(request.form['login'], request.form['password']):
            error = 'Credenciales inválidas'
        else:
            return redirect(url_for('inicio'))
    return render_template('login.html', error=error)

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    error = None
    if request.method == 'POST':
        if not autenticacion.crear_usuario(request.form['login'], request.form['password']):
            error = 'No se pudo crear el usuario'
        else:
            return redirect(url_for('inicio'))
    return render_template('registro.html', error=error)


@app.route('/inicio', methods=['GET', 'POST'])
def inicio():
    lista_producto = producto.buscar_productos()
    if request.method == 'POST':
        busqueda = request.form['busqueda']
        lista_filtrada= []
        for p in lista_producto:
            if p["titulo"] == busqueda:
                lista_filtrada.append(p)
        lista_producto = lista_producto


    return render_template('inicio.html', producto=lista_producto)


@app.route('/carrito', methods=['GET', 'POST'])
def carrito():
    return render_template('carrito.html')

@app.route('/comparador', methods=['GET', 'POST'])
def comparador():
    return render_template('comparador.html')


if __name__ == '__main__':
    app.debug = True
    app.run(port=5002)
