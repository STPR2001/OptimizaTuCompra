import requests

from web.servicios import rest_api

def buscar_productos():
    respuesta = requests.get(f'{rest_api.API_URL}/producto')
    return respuesta.json()
