import unittest
from app import format_leaf_results


class ReadLeafShould(unittest.TestCase):
    def test_format_result_into_dictionary(self):
        # Arrange
        path = "i/like/potatoes"
        text = "test"
        input_vars = [path, text]

        # Act
        result = format_leaf_results(input_vars)

        # Assert
        assert result['path'] == path
        assert result['text'] == text