from flask import Blueprint, render_template, jsonify
import requests

main = Blueprint('main', __name__)

# Ruta para la página principal
@main.route('/')
def index():
    return render_template('index.html')

# Ruta para la página de Imágenes del Día
@main.route('/Imagenes_del_Dia')
def imagenes_del_dia():
    api_url = 'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key': 'YCN3Afvnayoo7OtmqYFBpqLmxShN7ebAP2UYECDN',
        'count': 5
    }
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        news_data = response.json()
    except requests.RequestException as e:
        news_data = []
        print(f"Error al obtener datos de la API de la NASA: {e}")
    return render_template('imagenes_del_dia.html', news=news_data)
