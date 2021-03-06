import unittest
from node import *
from binary_search_tree import *

def is_leaf_node(node):
    return node.get_left() is None and node.get_right() is None

class TestBinarySearchTree(unittest.TestCase):

    """__init__ and insert tests"""
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
        root_right_child = root.get_right()

        # Depth 0
        self.assertIsNone(root.get_left())
        # Depth 1
        self.assertEqual(root_right_child.get_value(), 3)
        self.assertTrue(is_leaf_node(root_right_child))
        self.assertEqual(root_right_child.get_parent(), root)

    def test_initiate_with_three_nodes_where_child_is_less_than_parent(self):
        new_nodes = create_nodes([3, 2, 1])
        bst = BinarySearchTree(new_nodes)
        root = bst.get_root()
        root_left_child = root.get_left()

        # Depth 0
        self.assertIsNone(root.get_right())
        # Depth 1
        self.assertEqual(root_left_child.get_value(), 2)
        self.assertIsNone(root_left_child.get_right())
        # Depth 2
        self.assertEqual(root_left_child.get_left().get_value(), 1)
        self.assertTrue(is_leaf_node(root_left_child.get_left()))
        self.assertEqual(root_left_child.get_left().get_parent(), root_left_child)

    def test_initiate_with_three_nodes_with_same_value(self):
        new_nodes = create_nodes([1, 1, 1])
        bst = BinarySearchTree(new_nodes)
        root = bst.get_root()
        root_left_child = root.get_left()

        # Depth 0
        self.assertIsNone(root.get_right())
        # Depth 1
        self.assertEqual(root_left_child.get_value(), 1)
        self.assertIsNone(root_left_child.get_right())
        # Depth 2
        self.assertEqual(root_left_child.get_left().get_value(), 1)
        self.assertTrue(is_leaf_node(root_left_child.get_left()))
        self.assertEqual(root_left_child.get_left().get_parent(), root_left_child)

    def test_init_with_three_nodes_with_one_less_than_root_and_other_greater_than_child_but_less_than_root(self):
        new_nodes = create_nodes([3, 1, 2])
        bst = BinarySearchTree(new_nodes)
        root = bst.get_root()
        root_left_child = root.get_left()

        # Depth 0
        self.assertIsNone(root.get_right())
        # Depth 1
        self.assertEqual(root_left_child.get_value(), 1)
        self.assertIsNone(root_left_child.get_left())
        # Depth 2
        self.assertEqual(root_left_child.get_right().get_value(), 2)
        self.assertTrue(is_leaf_node(root_left_child.get_right()))
        self.assertEqual(root_left_child.get_right().get_parent(), root_left_child)

    def test_init_with_three_nodes_first_insert_less_than_root_and_next_insert_greater_than_root(self):
        new_nodes = create_nodes([2, 1, 3])
        bst = BinarySearchTree(new_nodes)
        root = bst.get_root()
        root_left_child = root.get_left()
        root_right_child = root.get_right()

        # Depth 1
        self.assertEqual(root_left_child.get_value(), 1)
        self.assertTrue(is_leaf_node(root_left_child))
        self.assertEqual(root_left_child.get_parent(), root)

        self.assertEqual(root_right_child.get_value(), 3)
        self.assertTrue(is_leaf_node(root_right_child))
        self.assertEqual(root_right_child.get_parent(), root)

    def test_init_with_three_nodes_first_insert_greater_than_root_and_next_insert_less_than_root(self):
        new_nodes = create_nodes([2, 3, 1])
        bst = BinarySearchTree(new_nodes)
        root = bst.get_root()
        root_left_child = root.get_left()
        root_right_child = root.get_right()

        # Depth 1
        self.assertEqual(root_left_child.get_value(), 1)
        self.assertTrue(is_leaf_node(root_left_child))
        self.assertEqual(root_left_child.get_parent(), root)

        self.assertEqual(root_right_child.get_value(), 3)
        self.assertTrue(is_leaf_node(root_right_child))
        self.assertEqual(root_right_child.get_parent(), root)

    def test_init_with_three_nodes_first_insert_greater_than_root_next_greater_than_root_but_less_than_child(self):
        new_nodes = create_nodes([1, 3, 2])
        bst = BinarySearchTree(new_nodes)
        root = bst.get_root()
        root_right_child = root.get_right()

        # Depth 1
        self.assertEqual(root_right_child.get_value(), 3)
        self.assertIsNone(root_right_child.get_right())
        # Depth 2
        self.assertEqual(root_right_child.get_left().get_value(), 2)
        self.assertTrue(is_leaf_node(root_right_child.get_left()))
        self.assertEqual(root_right_child.get_left().get_parent(), root_right_child)

    def test_init_with_three_nodes_with_two_nodes_same_value_and_greater_than_root(self):
        new_nodes = create_nodes([1, 2, 2])
        bst = BinarySearchTree(new_nodes)
        root = bst.get_root()
        root_right_child = root.get_right()

        # Depth 1
        self.assertEqual(root_right_child.get_value(), 2)
        self.assertIsNone(root_right_child.get_right())
        # Depth 2
        self.assertEqual(root_right_child.get_left().get_value(), 2)
        self.assertTrue(is_leaf_node(root_right_child.get_left()))
        self.assertEqual(root_right_child.get_left().get_parent(), root_right_child)

    def test_init_with_three_nodes_where_child_is_greater_than_parent(self):
        new_nodes = create_nodes([1, 2, 3])
        bst = BinarySearchTree(new_nodes)
        root = bst.get_root()
        root_right_child = root.get_right()

        # Depth 1
        self.assertEqual(root_right_child.get_value(), 2)
        self.assertIsNone(root_right_child.get_left())
        # Depth 2
        self.assertEqual(root_right_child.get_right().get_value(), 3)
        self.assertTrue(is_leaf_node(root_right_child.get_right()))
        self.assertEqual(root_right_child.get_right().get_parent(), root_right_child)

    """BFS Test"""
    def test_bfs_empty_bst(self):
        bst = BinarySearchTree()

        self.assertIsNone(bst.bfs(1))

    def test_bfs_size_one_bst_when_target_is_root(self):
        new_node = Node(1)
        bst = BinarySearchTree([new_node])

        self.assertEqual(bst.bfs(1), new_node)

    def test_bfs_size_three_bst_with_root_left_child_target(self):
        new_nodes = create_nodes([2, 1, 3])
        bst = BinarySearchTree(new_nodes)

        self.assertEqual(bst.bfs(1), new_nodes[1])

    def test_bfs_size_three_bst_with_root_right_child_target(self):
        new_nodes = create_nodes([2, 1, 3])
        bst = BinarySearchTree(new_nodes)

        self.assertEqual(bst.bfs(3), new_nodes[2])

    def test_bfs_with_left_only_children_bst_with_depth_2_target(self):
        new_nodes = create_nodes([3, 2, 1])
        bst = BinarySearchTree(new_nodes)

        self.assertEqual(bst.bfs(1), new_nodes[2])

    def test_bfs_with_right_only_children_bst_with_depth_2_target(self):
        new_nodes = create_nodes([1, 2, 3])
        bst = BinarySearchTree(new_nodes)

        self.assertEqual(bst.bfs(3), new_nodes[2])

    def test_bfs_with_target_being_right_child_of_root_left_child(self):
        new_nodes = create_nodes([3, 1, 2])
        bst = BinarySearchTree(new_nodes)

        self.assertEqual(bst.bfs(2), new_nodes[2])

    def test_bfs_with_target_being_left_child_of_root_right_child(self):
        new_nodes = create_nodes([1, 3, 2])
        bst = BinarySearchTree(new_nodes)

        self.assertEqual(bst.bfs(2), new_nodes[2])

    """delete tests"""
    # def test_delete_node_empty_bst(self):
    #
    # def test_delete_size_one_bst(self):


if __name__ == '__main__':
    unittest.main()
