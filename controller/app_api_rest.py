from flask import request, jsonify
from marshmallow import Schema, fields, post_load

from domain.contact import Contact, ContactTrace


class AppApiRest:

    def __init__(self, app):

        @app.route("/contact.json", methods=['POST'])
        def api_contact():
            contact_schema = ContactSchema().load(request.json)
            if contact_schema.errors:
                return jsonify(contact_schema.errors), 400
            contact_new = contact_schema.data

            contacts_find = Contact.query.filter_by(email=contact_new.email)
            if contacts_find.first():
                contact_new.id = contacts_find.first().id
                contact_new.update()
                contact = contact_new
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
    email = fields.Email(required=True)
    contacttrace = fields.Nested(ContactTraceSchema, many=True, load_only=True)

    @post_load
    def make_user(self, data):
        return Contact(**data)
