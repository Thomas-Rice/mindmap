import unittest
from app import create_mind_map


class CreateMindMapShould(unittest.TestCase):

    def test_create_mind_map_model_with_given_name(self):
        # Arrange
        mind_map_name = "testMap"

        # Act
        result = create_mind_map(mind_map_name)

        # Assert
        assert result.name == mind_map_name

    def test_error_if_name_is_not_a_string(self):
        # Arrange
        mind_map_name = 1

        # Assert
        self.assertRaises(Exception, lambda: create_mind_map(mind_map_name))
