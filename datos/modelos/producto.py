from datos.base_de_datos import BaseDeDatos

def crear_prodcuto(nombre, descripcion, precio):
    crear_prodcuto_sql = f"""
        INSERT INTO PRODUCTOS(NOMBRE, DESCRIPCION, PRECIO)
        VALUES ('{nombre}','{descripcion}','{precio}')
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(crear_prodcuto_sql)

def buscar_prodcuto(id_producto):
    buscar_producto_sql = f"""
        SELECT id_producto, nombre, descripcion, precio 
        FROM PRODUCTOS
        WHERE ID_PRODUCTO='{id_producto}'
    """
    bd = BaseDeDatos()
    return [{"id_producto": registro[0],
             "nombre": registro[1],
             "descripcion": registro[2],
             "precio": registro[3]
             } for registro in bd.ejecutar_sql(buscar_producto_sql)]

def borrar_usuario(id_producto):
    borrar_producto_sql = f"""
        DELETE
        FROM PRODUCTOS 
        WHERE ID_PRODUCTO = {id_producto}
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(borrar_producto_sql)

def buscar_prodcutos():
    buscar_producto_sql = f"""
        SELECT id_producto, nombre, descripcion, precio 
        FROM PRODUCTOS
    """
    bd = BaseDeDatos()
    return [{"id_producto": registro[0],
             "nombre": registro[1],
             "descripcion": registro[2],
             "precio": registro[3]
             } for registro in bd.ejecutar_sql(buscar_producto_sql)]

def modificar_producto(id_producto, datos_usuario):
    modificar_usuario_sql = f"""
        UPDATE PRODUCTOS
        SET NOMBRE='{datos_usuario["nombre"]}', DESCRIPCION='{datos_usuario["descripcion"]}', PRECIO='{datos_usuario["precio"]}'
        WHERE ID_PRODUCTO='{id_producto}'
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(modificar_usuario_sql)