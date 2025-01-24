#aca inicialmente vamos a poner la conexion a la base de datos para que podamos interactuar con ella

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

class DataBase:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        self.db = SQLAlchemy()
        self.is_initialized = False # sabemos que por defecto no esta inicializado

    def init_app(self, app): # inicializamos la base de datos
        if self.is_initialized: # verificamos si vemos que ya esta inicializada la base de datos
            raise RuntimeError("Database is already initialized")
        self.db.init_app(app) #COnecta la base de datos con la aplicacion
        self.is_initialized = True # cambiamos el estado de la base de datos a inicializado para que no se vuelva a inicializar

    def test_connection(self):
        try:
            with self.db.engine.connect() as connection:
                connection.execute(text("SELECT 1"))
            print("Database connection successful")
        except Exception as e:
            print(f"Database connection failed: {e}")

    def close_session(self, session):
        try:
            session.close()
        except Exception as e:
            print(f"Error closing session: {e}")
#inicializamos la base de datos globalmente para que sea visible en toda la aplicacion

db_instance = DataBase()
db = db_instance.db # db es la instancia de la base de datos que vamos a utilizar en toda la aplicacion
