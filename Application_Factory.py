from flask import Flask
from flask_sqlalchemy import SQLAlchemy


class Application_Factory:

    def create_app(self):
        app = Flask(__name__)

        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

        return app

    def init_db(self, app):
        return SQLAlchemy(app)
