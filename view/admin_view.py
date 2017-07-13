from flask_admin import Admin
from flask_admin.contrib.sqla.view import ModelView

from domain.contact import Contact, ContactTrace
from domain.db_connection import db


class ContactView(ModelView):
    page_size = 50
    column_editable_list = ['email']
    form_excluded_columns = ['created_at', 'updated_at']


class ContactTraceView(ModelView):
    page_size = 50
    form_excluded_columns = ['created_at', 'updated_at']


class AppAdminView:

    def __init__(self, app):
        admin = Admin(app, name='Rastreamento de usuários', template_mode='bootstrap3')
        admin.add_view(ContactView(Contact, db.session, name='Contato'))
        admin.add_view(ContactTraceView(ContactTrace, db.session, name='Rastro do contato'))
