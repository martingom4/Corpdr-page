#TODO 1: Crear archivo de configuración para la base de datos y el .env
import os
from dotenv import load_dotenv
from sqlalchemy import text

# Asegurarse de que el archivo .env esté guardado con codificación UTF-8
try:
    load_dotenv(dotenv_path='../../.env', encoding='utf-8')
except Exception as e:
    print(f"Error loading .env file: {e}")

class Config:
    DB_DRIVER = os.getenv('DB_DRIVER', 'postgresql+psycopg2')
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = os.getenv('DB_PORT', '5432')
    DB_USER = os.getenv('DB_USER', 'username')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')
    DB_NAME = os.getenv('DB_NAME', 'dbname')


    SQLALCHEMY_DATABASE_URI = f"{DB_DRIVER}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
