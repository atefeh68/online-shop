from flask import Flask
from blueprint.general import app as general
from blueprint.admin import app as admin
from flask_sqlalchemy import SQLAlchemy
import config
app = Flask(__name__)
app.register_blueprint(general)
app.register_blueprint(admin)

from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
db.init_app(app)

with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run()
