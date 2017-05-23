# import pdb
import argparse

from node import *

class BinarySearchTree:
    def __init__(self, nodes: 'list of Nodes'):
        self.root = None

        for node in nodes:
            self.insert(node)

    def get_root(self):
        return self.root

    def insert(self, new_node: Node):
        # pdb.set_trace()

        if self.root is None: # Set root
            self.root = new_node
        else:
            return self._insert(self.root, new_node)

    def _insert(self, root: Node, new_node: Node):
        # pdb.set_trace()

        if new_node.get_value() <= root.get_value(): # Less than or equal to root, insert new_node to left
            if not root.has_left():
                root.set_left(new_node)
                new_node.set_parent(root)
            else:
                return self._insert(root.get_left(), new_node)
        else: # Greater than root, insert new_node to right
            if not root.has_right():
                root.set_right(new_node)
                new_node.set_parent(root)
            else:
                return self._insert(root.get_right(), new_node)

if __name__ == "__main__":

    # Parse terminal command for values list
    parser = argparse.ArgumentParser()
    parser.add_argument('--i', )
    parser.add_argument('--values', nargs='*', type=int)
    args = parser.parse_args()

    nodes = create_nodes(args.values)

    bst = BinarySearchTree(nodes)
