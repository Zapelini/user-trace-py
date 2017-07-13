import json
import unittest
from http import HTTPStatus

from config.app import create_app


class ContactCrudTest(unittest.TestCase):

    def setUp(self):
        app = create_app("config.default.Testing")
        self.app = app.test_client()
        self.app.testing = True
        self.headers = [('Content-Type', 'application/json')]

        contact_response = self.app.post('/api/contact', headers=self.headers,
                                         data=json.dumps({"email": "mariobros@fulano.com"}))
        self.contact_json = json.loads(contact_response.data.decode('utf-8'))

    def test_get_all_contacts(self):
        quote = {"email": "mariobros@fulano.com"}
        self.app.post('/api/contact', headers=self.headers, data=json.dumps(quote))

        response = self.app.get('/api/contact')
        response_json = json.loads(response.data.decode('utf-8'))
        self.assertEqual(1, len(response_json['objects']))
