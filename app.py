from flask import Flask
from blueprint.general import app as general

app = Flask(__name__)
app.register_blueprint(general)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
