"""
Script criado para viabilizar a migração usando Flask-migrate com uma instancia limpa do Flask.

Ao usar a app do Flask que contém as demais extensões as migrações não são realizadas.

"""
from flask import Flask

from flask_migrate import Migrate
from domain.db_connection import db

app = Flask(__name__)
app.config.from_object('config.default.Production')
migrate = Migrate(app, db)
