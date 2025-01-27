from config import config
from src import init_app
from src.database.db import Base, engine  # Importar la base y el motor de SQLAlchemy




configuration = config['development']
app = init_app(configuration)

if __name__ == '__main__':
    app.run()
