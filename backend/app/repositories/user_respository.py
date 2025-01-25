from app.db import db
from app.models.user import User
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

bcrypt = Bcrypt()
class UserRepository:  # Corrige el nombre de la clase (convención PascalCase)

    def create_user(self, username, email, password):
        """Crea un nuevo usuario si los datos son válidos y no están duplicados."""
        self.validate_user(username, email, password)  # Lanza error si los campos son inválidos
        if not self.user_unique(username, email):  # Verifica si el usuario o email ya existen
            raise ValueError("User or email already exists")
        # Crea y guarda el usuario en la base de datos
        hashed_password =self.hash_password(password) # encriptamos la contraseña
        new_user = User(username=username, email=email, password=hashed_password) # creamos un nuevo usuario con password encriptado
        db.session.add(new_user)
        db.session.commit()

        return new_user

    def user_unique(self, username, email):#esto es para verificar si el usuario o el email ya existen en la base de datos
        """Verifica si el username o email ya existen en la base de datos."""
        existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
        return existing_user is None  # Retorna True si no existe, False si ya existe


    def validate_user(self, username, email, password): #esto es para verificar que los campos no esten vacios
        """Valida que los campos no estén vacíos."""
        if not username:
            raise ValueError("Username is required")
        if not email:
            raise ValueError("Email is required")
        if not password:
            raise ValueError("Password is required")


    # seria buenos crear un metodo para hashear la contraseña del usuario? no se si es necesario por el momento pero podriamos hacerlo
    def hash_password(self, password):
        return bcrypt.generate_password_hash(password).decode("utf-8")

    def authenticate_user(self, email, password): #esto es para autenticar al usuario y devolver un token JWT 
        """Autentica al usuario verificando su contraseña y devuelve un token JWT."""
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            token = create_access_token(identity=user.id)
            return token
        return None
