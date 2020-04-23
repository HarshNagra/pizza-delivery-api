from flask import Flask
from flask.blueprints import Blueprint

import config
import routes
from models import db

app = Flask(__name__)

app.debug = config.DEBUG
app.config["SQLALCHEMY_DATABASE_URI"] = config.DB_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config.SQLALCHEMY_TRACK_MODIFICATIONS
app.config["SQLALCHEMY_SCRIPT_LOCATION"] = config.SQLALCHEMY_SCRIPT_LOCATION
app.url_map.strict_slashes = False
db.init_app(app)
db.app = app

for blueprint in vars(routes).values():
    if isinstance(blueprint, Blueprint):
        app.register_blueprint(blueprint, url_prefix=config.APPLICATION_ROOT)

if __name__ == "__main__":
    app.run(host=config.HOST, port=config.PORT)
