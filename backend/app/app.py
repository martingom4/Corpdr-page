#aca debemos de inicializar la base de datos con la aplicacion de flask
from flask import Flask
from app.db import db_instance, db
from config import Config  # Importamos la configuración
#TODO instalar flask-migrate
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)

    # Cargar configuración desde config.py
    app.config.from_object(Config) # cargamos la configuracion desde el archivo config.py que acabamos de crear 

    # Inicializar la base de datos
    db_instance.init_app(app)

    # Configurar Flask-Migrate para manejar migraciones
    Migrate(app, db)

    return app  # Retornar la aplicación sin crear tablas manualmente
