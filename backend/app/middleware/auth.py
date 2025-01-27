# lo que tengo que investigar es como se usa esto y como funciona esto para poder tener seguridad
#documentacion para la mejora de este codigo
from repositories import UserRepository
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token

User = UserRepository()
bcrypt = Bcrypt()
class auth: # aca vamos a crear una funcion para la autenticacion de los usuarios
    #yo aca tambien puedo hashear la contraseña no se que tan practico sea pero lo hare
    def hash_password(self, password):
        return bcrypt.generate_password_hash(password).decode("utf-8")

    def authenticate_user(self, email, password): #esto es para autenticar al usuario y devolver un token JWT
        """Autentica al usuario verificando su contraseña y devuelve un token JWT."""
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            token = create_access_token(identity=user.id)
            return token
        return None

