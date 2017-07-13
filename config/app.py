from flask import Flask

from controller.app_api_rest import AppApiRest
from domain.db_connection import db
from view.admin_view import AppAdminView


def create_app(config_name):

    app = Flask(__name__)
    app.config.from_object(config_name)

    app.config['SESSION_TYPE'] = 'memcached'
    app.config['SECRET_KEY'] = 'super secret key'

    with app.app_context():
        db.init_app(app)
        if app.config['IS_LOCAL_DATABASE']:
            db.create_all()

    with app.app_context():
        # ContactApi(app)
        AppApiRest(app)

    AppAdminView(app)

    return app
