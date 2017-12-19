from flask import Blueprint

messages_blueprint = Blueprint(
    'messages',
    __name__,
    template_folder='templates'
)
