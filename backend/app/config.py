#TODO 1: Crear archivo de configuración para la base de datos y el .env

import os
from dotenv import load_dotenv

# Cargar variables de entorno desde un archivo .env
load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://username:password@localhost/dbname')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
