import unittest
from app import split_path, Leaf, create_node_tree, Node

# missing more tests to test if parent nodes are correct - ran out fo time
class PrintShould(unittest.TestCase):

    def test_split_path_with_two_leafs(self):
        # Arrange
        path1 = "i/like/potatoes"
        path2 = "you/eat/eggs"
        expected_result_1 = ['i', 'like', 'potatoes']
        expected_result_2 = ['you', 'eat', 'eggs']
        leaf1 = Leaf(path=path1, text="lol")
        leaf2 = Leaf(path=path2, text="haha")
        result = [leaf1, leaf2]

        # Act
        result = split_path(result)

        # Assert
        assert result[0] == expected_result_1
        assert result[1] == expected_result_2

    def test_create_node_tree(self):
        # Arrange
        path1 = "i/like/potatoes"
        path2 = "you/eat/eggs"
        expected_result = ["Test",
                           "i",
                           "like",
                           "potatoes",
                           "you",
                           "eat",
                           "eggs"]
        leaf1 = Leaf(path=path1, text="lol")
        leaf2 = Leaf(path=path2, text="haha")
        result = [leaf1, leaf2]
        result = split_path(result)
        map_name = 'Test'

        # Act
        result = create_node_tree(map_name=map_name, leafs=result)

        # Assert
        for i, element in enumerate(result):
            assert element.name == expected_result[i]








