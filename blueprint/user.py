from flask import Blueprint
import models.user

app = Blueprint("user",__name__)


@app.route('/user')
def index():
    return "user"