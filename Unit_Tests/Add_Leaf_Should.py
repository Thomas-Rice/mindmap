import unittest
from app import create_leaf


class AddLeafShould(unittest.TestCase):

    def test_create_lead_model_with_parameters(self):
        # Arrange
        mind_map_name = "testMap"
        path = "i/like/hotdogs"
        text = "haha"

        # Act
        result = create_leaf(mind_map_name, path, text)

        # Assert
        assert result.map_name == mind_map_name
        assert result.path == path
        assert result.text == text

    def test_error_if_path_is_not_a_string(self):
        # Arrange
        mind_map_name = "testMap"
        path = 1
        text = "haha"

        # Assert
        self.assertRaises(Exception, lambda: create_leaf(mind_map_name, path, text))

    def test_error_if_text_is_not_a_string(self):
        # Arrange
        mind_map_name = "testMap"
        path = "i/like/hotdogs"
        text = 1

        # Assert
        self.assertRaises(Exception, lambda: create_leaf(mind_map_name, path, text))

    def test_error_if_text_and_path_are_not_a_string(self):
        # Arrange
        mind_map_name = "testMap"
        path = 1
        text = 1

        # Assert
        self.assertRaises(Exception, lambda: create_leaf(mind_map_name, path, text))

