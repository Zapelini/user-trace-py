from flask import request
from marshmallow import Schema, fields, post_load

from domain.contact import Contact, ContactTrace


class AppApiRest:

    def __init__(self, app):

        @app.route("/contact.json", methods=['POST'])
        def api_contact():
            contact_new = ContactSchema().load(request.json).data
            contacts_find = Contact.query.filter_by(email=contact_new.email)
            if contacts_find.first():
                # contact = contacts_find.first()
                # contact.contacttrace = contact_new.contacttrace
                # contact.update()
                contacts_find.first().update({"contacttrace": contact_new.contacttrace})
                # contacttrace = contact_new.contacttrace
                # contacttrace.contact_id = contacts_find.first().id
                # contacttrace.save()
            else:
                contact = contact_new
                contact.save()
            return ContactSchema().dumps(contact).data, 201


class ContactTraceSchema(Schema):
    url = fields.Str()
    date_access = fields.DateTime()

    @post_load
    def make_user(self, data):
        return ContactTrace(**data)


class ContactSchema(Schema):
    id = fields.Integer(dump_only=True)
    email = fields.Email()
    contacttrace = fields.Nested(ContactTraceSchema, many=True, load_only=True)

    @post_load
    def make_user(self, data):
        return Contact(**data)
