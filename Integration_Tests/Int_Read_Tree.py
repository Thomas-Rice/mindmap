import unittest

from app import *


class IntegrationReadTree(unittest.TestCase):

    def setup_test(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.sqlite3'
        app.config['TESTING'] = True
        client = app.test_client()

        db.drop_all()
        db.create_all()
        return client


    # TODO All responses should be decoded to strings
    # TODO Use Messages Class instead of strings
    def test_read_tree(self):
        client = self.setup_test()
        # Create Mind Map
        map_name = "int-test"
        response = client.post('/api/maps', json={'id': map_name})

        assert b'Created MindMap with name: int-test ' in response.data

        # Add Leaf
        path = "int-test/lol/super"
        text = "random text"

        response = client.post(f'/api/maps/{map_name}', json={'path': path, "text": text})

        assert b'Created Leaf in MindMap: int-test with path: int-test/lol/super and text: random text ' in response.data
        assert response.status == "200 OK"

        response = client.get(f'/api/maps/{map_name}?pretty=true')

        assert b'\nint-test\n\xe2\x94\x94\xe2\x94\x80\xe2\x94\x80 int-test\n    \xe2\x94\x94\xe2\x94\x80\xe2\x94\x80 lol\n        \xe2\x94\x94\xe2\x94\x80\xe2\x94\x80 super' in response.data
        assert response.status == "200 OK"

    def test_map_does_not_exist(self):
        client = self.setup_test()

        response = client.get(f'/api/maps/nonexistentmap?pretty=true')
        print(response.data)
        assert b'No Results Found for Given Map Name - Check If Map Exists' in response.data
        assert response.status == "200 OK"
