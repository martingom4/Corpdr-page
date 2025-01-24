#aca debemos de inicializar la base de datos con la aplicacion de flask
from flask import Flask
from app.db import db_instance, db
from app.config import Config  # Importamos la configuración
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)
    # Cargar configuración desde config.py
    app.config.from_object(Config) # cargamos la configuracion desde el archivo config.py que acabamos de crear
    # Inicializar la base de datos
    db_instance.init_app(app)
    with app.app_context():
        try:
            db_instance.test_connection()  # Probar la conexión a la base de datos dentro del contexto de la aplicación
        except Exception as e:
            print(f"Error during database connection test: {e}")
    # Configurar Flask-Migrate para manejar migraciones
    Migrate(app, db) #hacemos la migracion de la base de datos
    return app  # Retornar la aplicación sin crear tablas manualmente
