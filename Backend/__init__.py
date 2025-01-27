#aca es donde pondremos los blueprints de nuestra aplicacion

from flask import Flask

from .routes import IndexRoutes

def init_app():
    app = Flask(__name__)

    #aca vamos a registrar los blueprints 
    app.register_blueprint(IndexRoutes)

    return app
