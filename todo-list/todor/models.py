# Importando la base de datos
from todor import db

# Creando clase para usuario
class User(db.Model):
    __tablename__ = 'users'  # Nombre de la tabla

    id = db.Column(db.Integer, primary_key=True)  # Identificador único
    username = db.Column(db.String(20), unique=True, nullable=False)  # Nombre de usuario
    password = db.Column(db.Text, nullable=False)  # Contraseña

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User {self.username}>'

# Creando clase para todo
class Todo(db.Model):
    __tablename__ = 'todos'  # Nombre de la tabla

    id = db.Column(db.Integer, primary_key=True)  # Identificador único
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # Relación con usuario
    title = db.Column(db.String(100), nullable=False)  # Título de la tarea
    desc = db.Column(db.Text)  # Descripción de la tarea
    state = db.Column(db.Boolean, default=False)  # Estado de la tarea

    def __init__(self, created_by, title, desc, state=False):
        self.created_by = created_by
        self.title = title
        self.desc = desc
        self.state = state

    def __repr__(self):
        return f'<Todo {self.title}>'
