from flask_restless import APIManager

from domain.contact import Contact
from domain.db_connection import db


class AppApiRest:

    def __init__(self, app):
        api = APIManager(app, flask_sqlalchemy_db=db)
        api.create_api(Contact, methods=['GET', 'POST'])
