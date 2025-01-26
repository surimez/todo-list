from flask import Flask, render_template
from .db import db  # Importamos db desde db.py
from .todo import bp as todo_bp  # Blueprint para tareas
from .auth import bp as auth_bp  # Blueprint para autenticación

def create_app():
    # Crear instancia de Flask
    app = Flask(__name__)  
    
    # Configuración de la aplicación
    app.config.from_mapping(
        DEBUG=True,
        SECRET_KEY='dev_esit',
        SQLALCHEMY_DATABASE_URI="sqlite:///todolist.db"  # Base de datos SQLite
    )
    
    # Iniciar la conexión de SQLAlchemy con la aplicación
    db.init_app(app)
    
    # Registrar los blueprints
    app.register_blueprint(todo_bp)
    app.register_blueprint(auth_bp)

    # Definir la ruta principal
    @app.route('/')
    def index():
        return render_template('index.html')
    
    # Crear las tablas en la base de datos (si no existen)
    with app.app_context():
        db.create_all()
    
    return app
