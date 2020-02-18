import unittest

from app import *


class IntegrationAddLeaf(unittest.TestCase):

    def setup_test(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.sqlite3'
        app.config['TESTING'] = True
        client = app.test_client()

        db.drop_all()
        db.create_all()
        return client

    def test_add_leaf_with_path_and_text(self):
        client = self.setup_test()
        map_name = "add_leaf_test_1"
        path = "int-test"
        text = "random text"

        response = client.post(f'/api/maps/{map_name}', json={'path': path, "text": text})

        assert b'Created Leaf in MindMap: add_leaf_test_1 with path: int-test and text: random text' in response.data
        assert response.status == "200 OK"

    def test_add_leaf_without_path_and_with_text(self):
        client = self.setup_test()
        map_name = "add_leaf_test_1"
        text = "random text"

        response = client.post(f'/api/maps/{map_name}', json={"text": text})

        assert b"This Request needs path and text data \n path: 'Test' \n text: 'Test'" in response.data

    def test_add_leaf_without_text_and_with_path(self):
        client = self.setup_test()
        map_name = "add_leaf_test_1"
        path = "int-test"

        response = client.post(f'/api/maps/{map_name}', json={"path": path})

        assert b"This Request needs path and text data \n path: 'Test' \n text: 'Test'" in response.data

    def test_add_leaf_without_path_or_text(self):
        client = self.setup_test()
        map_name = "add_leaf_test_1"

        response = client.post(f'/api/maps/{map_name}', json={})

        assert b"This Request needs path and text data \n path: 'Test' \n text: 'Test'" in response.data

