# Importando Blueprint
from flask import Blueprint
from . import models

# Creando instancia
bp = Blueprint('auth', __name__, url_prefix='/auth')

# Creando ruta y función
@bp.route('/register')
def register():
    return "Registrar usuario"

@bp.route('/login')
def login():
    return "Iniciar sesión"
