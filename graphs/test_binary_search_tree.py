import unittest
from node import *
from binary_search_tree import *

def is_leaf_node(node):
    return node.get_left() is None and node.get_right() is None

class TestBinarySearchTree(unittest.TestCase):

    #Initiate empty BST
    def test_initiate_empty_bst(self):
        bst = BinarySearchTree()

        self.assertIsNone(bst.get_root())

    def test_initiate_with_one_node(self):
        new_node = Node(1)
        bst = BinarySearchTree([new_node])
        root = bst.get_root()

        self.assertEqual(root.get_value(), 1)
        self.assertTrue(is_leaf_node(root))
        self.assertIsNone(root.get_parent())

    def test_initiate_with_two_nodes_one_less_than_root(self):
        new_nodes = create_nodes([2, 1])
        bst = BinarySearchTree(new_nodes)
        root = bst.get_root()
        root_left_child = root.get_left()

        # Depth 0
        self.assertIsNone(root.get_right())
        # Depth 1
        self.assertEqual(root_left_child.get_value(), 1)
        self.assertTrue(is_leaf_node(root_left_child))
        self.assertEqual(root_left_child.get_parent(), root)

    def test_initiate_with_two_nodes_with_same_value(self):
        new_nodes = create_nodes([2, 2])
        bst = BinarySearchTree(new_nodes)
        root = bst.get_root()
        root_left_child = root.get_left()

        # Depth 0
        self.assertIsNone(root.get_right())
        # Depth 1
        self.assertEqual(root_left_child.get_value(), 2)
        self.assertTrue(is_leaf_node(root_left_child))
        self.assertEqual(root_left_child.get_parent(), root)

    def test_initiate_with_two_nodes_one_greater_than_root(self):
        new_nodes = create_nodes([2, 3])
        bst = BinarySearchTree(new_nodes)
        root = bst.get_root()
        root_right_node = root.get_right()

        # Depth 0
        self.assertIsNone(root.get_left())
        # Depth 1
        self.assertEqual(root_right_node.get_value(), 3)
        self.assertTrue(is_leaf_node(root_right_node))
        self.assertEqual(root_right_node.get_parent(), root)

    def test_initiate_with_three_nodes_where_child_is_less_than_parent(self):
        new_nodes = create_nodes([3, 2, 1])
        bst = BinarySearchTree(new_nodes)
        root = bst.get_root()
        root_left_child = root.get_left()

        # Depth 0
        self.assertIsNone(root.get_right())
        # Depth 1
        self.assertEqual(root_left_child.get_value(), 2)
        self.assertIsNone(root_left_child.get_parent().get_right())
        # Depth 2
        self.assertEqual(root_left_child.get_left().get_value(), 1)
        self.assertTrue(is_leaf_node(root_left_child.get_left()))
        self.assertEqual(root_left_child.get_left().get_parent(), root_left_child)

if __name__ == '__main__':
    unittest.main()
