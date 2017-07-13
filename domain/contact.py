import datetime

from domain.db_connection import db


class Contact(db.Model):
    __tablename__ = 'contact'

    id = db.Column(db.Integer, db.Sequence('contact_id_seq', start=1), primary_key=True)
    email = db.Column(db.String(100), unique=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow())
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow())

    def __str__(self):
        return self.email


class ContactTrace(db.Model):
    __tablename__ = 'contacttrace'

    id = db.Column(db.Integer, db.Sequence('contatcttrace_id_seq', start=1), primary_key=True)
    url = db.Column(db.String(1000), nullable=False)
    date_access = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow())
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow())

    contact_id = db.Column(db.Integer, db.ForeignKey('contact.id'))
    contact = db.relationship('Contact', backref=db.backref('contacttrace', lazy='dynamic'))

    def __str__(self):
        return '{0} {1}'.format(self.url, self.contact_id)
