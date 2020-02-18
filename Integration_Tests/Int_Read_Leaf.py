import unittest

from app import *


class IntegrationReadLeaf(unittest.TestCase):

    def setup_test(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.sqlite3'
        app.config['TESTING'] = True
        client = app.test_client()

        db.drop_all()
        db.create_all()
        return client

    def test_read_leaf_with_path(self):
        client = self.setup_test()
        map_name = "add_leaf_test_1"
        path = "int/test"
        text = "random text"

        # Create Row
        response = client.post(f'/api/maps/{map_name}', json={"path": path, "text": text})

        assert b'Created Leaf in MindMap: add_leaf_test_1 with path: int/test and text: random text' in response.data
        assert response.status == "200 OK"

        # Read Row
        response = client.get(f'/api/maps/{map_name}/{path}')

        assert b'{"path":"int/test","text":"random text"}\n' in response.data
        assert response.status == "200 OK"

    def test_read_leaf_with_non_existent_path(self):
        client = self.setup_test()
        map_name = "add_leaf_test_1"
        path = "none"

        # Read Row
        response = client.get(f'/api/maps/{map_name}/{path}')

        assert b'No Results Found For The Combination Of Map ID and Path - Please Use Check Map ID & Path Are Correct' in response.data
        assert response.status == "200 OK"

    def test_read_leaf_with_non_existant_map_id_and_path(self):
        client = self.setup_test()
        map_name = "none"
        path = "none"

        # Read Row
        response = client.get(f'/api/maps/{map_name}/{path}')

        assert b'No Results Found For The Combination Of Map ID and Path - Please Use Check Map ID & Path Are Correct' in response.data
        assert response.status == "200 OK"

    def test_read_leaf_with_non_existent_map_id_and_path(self):
        client = self.setup_test()
        map_name = "none"
        path = "none"

        # Read Row
        response = client.get(f'/api/maps/{map_name}/{path}')

        assert b'No Results Found For The Combination Of Map ID and Path - Please Use Check Map ID & Path Are Correct' in response.data
        assert response.status == "200 OK"
