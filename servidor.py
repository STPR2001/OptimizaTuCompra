from flask import Flask, request, jsonify
from servicios.autenticacion import autenticacion
from servicios.usuario_producto import producto_s
from flask import render_template


app = Flask(__name__)

#PAGINA PRINCIPAL

@app.route('/')
def get_index():
    titulo_pag = 'OptimizaTuCompra'
    return render_template('login.html', titulo=titulo_pag)

#USUARIOS

#CREAR USUARIO
@app.route('/usuarios', methods=['POST'])
def crear_usuario():
    datos_usuario = request.get_json()
    if 'nombre' not in datos_usuario or datos_usuario['nombre'] == '':
        return 'El nombre de usuario es requerido', 412
    if 'clave' not in datos_usuario:
        return 'La clave es requerida', 412
    try:
        autenticacion.crear_usuario(datos_usuario['nombre'], datos_usuario['clave'])
    except Exception:
        return 'El usuario ya existe', 412
    return 'OK', 200

#MODIFICAR USUARIO
@app.route('/usuarios/<id_usuario>', methods=['PUT'])
def modificar_usuario(id_usuario):
    datos_usuario = request.get_json()
    if 'nombre' not in datos_usuario or datos_usuario['nombre'] == '':
        return 'El nombre de usuario es requerido', 412
    if 'clave' not in datos_usuario:
        return 'La clave es requerida', 412
    autenticacion.modificar_usuario(id_usuario, datos_usuario)
    return 'OK', 200

#OBTENER USUARIOS
@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    return jsonify(autenticacion.obtener_usuarios())

#OBTENER USUARIO
@app.route('/usuarios/<id_usuario>', methods=['GET'])
def obtener_usuario(id_usuario):
    try:
        usuario = autenticacion.obtener_usuario(id_usuario)
        return jsonify(usuario)
    except Exception:
        return 'Usuario no encontrado', 404

#BORRAR USUARIO
@app.route('/usuarios/<id_usuario>', methods=['DELETE'])
def borrar_usuario(id_usuario):
    autenticacion.borrar_usuario(id_usuario)
    return "Borrado", 200

#INICIAR SESION
@app.route('/login', methods=['POST'])
def login():
    datos_usuario = request.get_json()
    if 'nombre' not in datos_usuario:
        return 'El nombre de usuario es requerido', 412
    if 'clave' not in datos_usuario:
        return 'La clave es requerida', 412
    try:
        id_sesion = autenticacion.login(datos_usuario['nombre'], datos_usuario['clave'])
        return jsonify({"id_sesion": id_sesion})
    except Exception:
        return 'USUARIO NO ENCONTRADO', 404

#PRODUCTOS

#CREAR PRODUCTO
@app.route('/producto', methods=['POST'])
def crear_producto():
    datos_producto = request.get_json()

    producto_s.crear_producto(datos_producto['nombre'], datos_producto['descripcion'], datos_producto ['precio'])
    return 'Producto agregado con exito', 200

#BUSCAR PRODUCTOS
@app.route('/producto', methods=['GET'])
def buscar_productos():
    return jsonify(producto_s.buscar_prodcutos())

#BUSCAR PRODUCTO
@app.route('/producto/<id_producto>', methods=['GET'])
def buscar_producto(id_producto):
    try:
        producto = producto_s.buscar_prodcuto(id_producto)
        return jsonify(producto)
    except Exception:
        return 'Producto no encontrado', 404

#BORRAR PRODUCTO
@app.route('/producto/<id_producto>', methods=['DELETE'])
def borrar_producto(id_producto):
    producto_s.borrar_producto(id_producto)
    return "Borrado", 200

#MODIFICAR PRODUCTO
@app.route('/producto/<id_producto>', methods=['PUT'])
def modificar_producto(id_producto):
    datos_usuario = request.get_json()
    if 'nombre' not in datos_usuario or datos_usuario['nombre'] == '':
        return 'El nombre de usuario es requerido', 412
    if 'descripcion' not in datos_usuario:
        return 'La descripcion es requerida', 412
    if "precio" not in datos_usuario:
        return 'El precio es requerido'
    producto_s.modificar_producto(id_producto, datos_usuario)
    return 'OK', 200

if __name__ == '__main__':
    app.debug = True
    app.run(port=5001)
