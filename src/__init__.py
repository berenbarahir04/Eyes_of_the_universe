from flask import Flask
from .routes import main as main_blueprint  # Importamos el blueprint de rutas

def create_app():
    app = Flask(__name__)
    
    # Configurar el blueprint de rutas
    app.register_blueprint(main_blueprint)

    return app
