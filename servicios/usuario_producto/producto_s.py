from datos.modelos import producto as modelo_producto

def crear_producto(nombre, descripcion, precio):
    modelo_producto.crear_prodcuto(nombre, descripcion, precio)

def buscar_prodcuto(id_producto):
    producto = modelo_producto.buscar_prodcuto(id_producto)
    if len(producto) == 0:
        raise Exception("El producto no existe")
    return producto[0]

def buscar_prodcutos():
    return modelo_producto.buscar_prodcutos()

def borrar_producto(id_producto):
    modelo_producto.borrar_usuario(id_producto)

def modificar_producto(id_producto, datos_usuario):
    modelo_producto.modificar_producto(id_producto, datos_usuario)