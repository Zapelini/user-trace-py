import datetime

from domain.db_connection import db


class Contact(db.Model):
    __tablename__ = 'contact'

    id = db.Column(db.Integer, db.Sequence('contact_id_seq', start=1), primary_key=True)
    email = db.Column(db.String(100), unique=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow())
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow())

    contacttrace = db.relationship("ContactTrace", back_populates="contact")

    def __str__(self):
        return self.email

    def save(self):
        with db.session.no_autoflush:
            db.session.add(self)
            db.session.commit()

    def update(self):
        with db.session.no_autoflush:
            db.session.merge(self)
            db.session.commit()


class ContactTrace(db.Model):
    __tablename__ = 'contacttrace'

    id = db.Column(db.Integer, db.Sequence('contatcttrace_id_seq', start=1), primary_key=True)
    url = db.Column(db.String(1000), nullable=False)
    date_access = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow())
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow())

    contact_id = db.Column(db.Integer, db.ForeignKey('contact.id'))
    contact = db.relationship("Contact", back_populates="contacttrace")

    def __str__(self):
        return '{0} {1}'.format(self.url, self.contact_id)

    def save(self):
        with db.session.no_autoflush:
            db.session.add(self)
            db.session.commit()
