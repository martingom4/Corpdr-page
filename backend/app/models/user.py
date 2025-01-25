# aca vamos a definir los modelos que vamos a utilizar en la base de datos y vamos a definir las relaciones entre ellos
# como primer tabla vamos a empezar con la de los usuarios, que necesitamos? 1. id, 2. username, 3. email, 4. password por el momento

from app.db import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False) # esta es la que tendra el hash de la contraseña del usuario que se registre
    
