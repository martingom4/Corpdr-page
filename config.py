from decouple import config

class Config:
    SECRET_KEY = config('SECRET_KEY') #aca se va a guardar la clave secreta de la aplicacion

class DevelopmentConfig(Config):
    DEBUG = True

config = {
    'development': DevelopmentConfig
}
