import pdb
import sys

from node import Node

class BinarySearchTree:
    def __init__(self, root: Node):
        self.root = root

    def get_root(self):
        return self.root

    def insert(self, root: Node, new_node: Node):
        pdb.set_trace()
        if new_node.get_value() <= root.get_value(): # Insert new_node to left of root
            if not root.has_left():
                root.set_left(new_node)
                new_node.set_parent(root)
            else:
                self.insert(root.get_left(), new_node)
        else: # Insert new_node to right of root
            if not root.has_right():
                root.set_right(new_node)
                new_node.set_parent(root)
            else:
                self.insert(root.get_right(), new_node)

if __name__ == "__main__":

    nodes = []
    nums = [6, 3 ,9, 5, 5, 7, 1]

    for num in nums:
        nodes.append(Node(num))

    bst = BinarySearchTree(root)

    for num in nums:
        bst.insert(bst.get_root(), Node(num))
