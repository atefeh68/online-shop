from flask import Blueprint

app = Blueprint('general', __name__)

@app.route('/')
def index():
    return "hello world"