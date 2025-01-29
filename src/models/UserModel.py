from sqlalchemy import Column, Integer, String
from src.database.db import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)
    name = Column(String)

    def __init__(self, username, password, name) -> None:
        self.username = username
        self.password = password
        self.name = name


#revisar lo que se hace para el inicio de sesion 

