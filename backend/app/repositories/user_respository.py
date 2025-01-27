from app.db import db
from app.models.user import User
from middleware import auth


class UserRepository:  # Corrige el nombre de la clase (convención PascalCase)

    def create_user(self, username, email, password):
        """Crea un nuevo usuario si los datos son válidos y no están duplicados."""
        self.validate_user(username, email, password)  # Lanza error si los campos son inválidos
        if not self.user_unique(username, email):  # Verifica si el usuario o email ya existen
            raise ValueError("User or email already exists")
        # Crea y guarda el usuario en la base de datos
        hashed_password = auth.hash_password(password) # encriptamos la contraseña
        new_user = User(username=username, email=email, password=hashed_password) # creamos un nuevo usuario con password encriptado
        db.session.add(new_user)
        db.session.commit()

        return new_user

    def user_unique(self, username, email):#esto es para verificar si el usuario o el email ya existen en la base de datos
        """Verifica si el username o email ya existen en la base de datos."""
        existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
        return existing_user is None  # Retorna True si no existe, False si ya existe


    def validate_user(self, username, email, password): #esto es para verificar que los campos no esten vacios es una buena idea pero no muestra que valor falta en caso de que falte alguno
        """Valida que los campos no estén vacíos."""
        if not all([username, email, password]):
            raise ValueError("All fields (username, email, password) are required")

    def get_user(self, id):
        """Obtiene el usuario por su ID."""
        user = User.query.get(id)
        if user is None:
            raise ValueError("User not found")
        return user  # Retorna el usuario con el ID especificado o lanza un error si no existe


