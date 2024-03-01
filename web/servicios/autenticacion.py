import requests

from web.servicios import rest_api


def validar_credenciales(usuario, clave):
    body = {"nombre": usuario,
            "clave": clave}
    respuesta = requests.post(f'{rest_api.API_URL}/login', json=body)
    # Solo verificamos el codigo de la respuesta en este caso
    return respuesta.status_code == 200


def crear_usuario(usuario, clave):
    body = {"nombre": usuario,
            "clave": clave}
    respuesta = requests.post(f'{rest_api.API_URL}/usuarios', json=body)
    # Al igual que en el caso de la validacion, simplificamos el manejo de errores
    return respuesta.status_code == 200


def obtener_usuarios():
    respuesta = requests.get(f'{rest_api.API_URL}/usuarios')
    return respuesta.json()
