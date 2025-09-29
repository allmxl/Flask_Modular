
from flask import Blueprint


main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    """Retorna a saudação principal."""
    return "Olá, Mundo!"

@main_bp.route('/sobre')
def sobre():
    nome = "Mel"
    return f"Olá, {nome}!"