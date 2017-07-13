import json
import unittest
from http import HTTPStatus

from config.app import create_app


class ApiContactTest(unittest.TestCase):

    def setUp(self):
        app = create_app("config.default.Testing")
        self.app = app.test_client()
        self.app.testing = True
        self.headers = [('Content-Type', 'application/json')]

    def test_create_contact_and_trace(self):
        data = {"email": "mariobros@fulano.com",
                     "contacttrace": [{"url": "preco", "date_access": "2017-12-07 13:03:57"}]}
        response = self.app.post('/contact.json', headers=self.headers, data=json.dumps(data))
        response_json = json.loads(response.data.decode('utf-8'))
        self.assertEqual(HTTPStatus.CREATED, response.status_code)
        self.assertEqual(response_json['email'], data['email'])
        self.assertEqual(1, response_json['id'])

    def test_create_contacttrate_to_contact(self):
        data = {"email": "mariobros@fulano.com",
                     "contacttrace": [{"url": "preco", "date_access": "2017-12-07 13:03:57"}]}
        response = self.app.post('/contact.json', headers=self.headers, data=json.dumps(data))
        response_json = json.loads(response.data.decode('utf-8'))
        self.assertEqual(HTTPStatus.CREATED, response.status_code)
        self.assertEqual(response_json['email'], data['email'])
        self.assertEqual(1, response_json['id'])

        data = {"email": "mariobros@fulano.com",
                "contacttrace": [{"url": "preco", "date_access": "2017-12-07 13:10:41"},
                                 {"url": "contato", "date_access": "2017-12-07 13:11:50"}]}
        response = self.app.post('/contact.json', headers=self.headers, data=json.dumps(data))
        response_json = json.loads(response.data.decode('utf-8'))
        self.assertEqual(HTTPStatus.CREATED, response.status_code)
        self.assertEqual(response_json['email'], data['email'])
        self.assertEqual(1, response_json['id'])
