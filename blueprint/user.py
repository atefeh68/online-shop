from flask import Blueprint

app = Blueprint("user",__name__)


@app.route('/user')
def index():
    return "user"