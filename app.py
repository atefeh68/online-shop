from flask import Flask
from blueprint.general import app as general
from blueprint.admin import app as admin
import extentions
import config
app = Flask(__name__)
app.register_blueprint(general)
app.register_blueprint(admin)



app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
extentions.db.init_app(app)

with app.app_context():
    extentions.db.create_all()


if __name__ == '__main__':
    app.run()
