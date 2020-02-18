import unittest

from app import *


class Integration(unittest.TestCase):

    def setup_test(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.sqlite3'
        app.config['TESTING'] = True
        client = app.test_client()

        db.drop_all()
        db.create_all()
        return client

    def test_create_mind_map_with_id(self):
        client = self.setup_test()
        name = "int-test"
        response = client.post('/api/maps', json={'id': name})

        assert b'Created MindMap with name: int-test ' in response.data

    def test_create_mind_map_with_no_id(self):
        client = self.setup_test()

        response = client.post('/api/maps', json={})

        assert b"<h1>id needs to be supplied in order to create a new mind map \n { 'id' : 'my-map'} </h1>" in response.data

    def test_create_mind_map_with_id_not_string(self):
        client = self.setup_test()
        id = 1

        response = client.post('/api/maps', json={'id': id})

        assert b"id must be of type string" in response.data

