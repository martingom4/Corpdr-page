from app.app import create_app
from app.db import db
from sqlalchemy.sql import text

# Crear la aplicación antes de acceder al contexto
app = create_app()

try:
    # ✅ Crear el contexto de la aplicación antes de acceder a la base de datos
    with app.app_context():
        with db.engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            print("✅ Conexión exitosa a la base de datos 🚀")
except Exception as e:
    print(f"❌ Error al conectar a la base de datos: {e}")
