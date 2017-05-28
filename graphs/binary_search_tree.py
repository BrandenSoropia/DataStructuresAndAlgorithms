# import pdb
import argparse

from node import *

class BinarySearchTree:
    def __init__(self, nodes=None):
        self.root = None

        if nodes is not None:
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

    def get_node_children(self, node: Node) -> list:
        children = []
        if node.has_left():
            children.append(node.get_left())

        if node.has_right():
            children.append(node.get_right())

        return children

    # Return first node matching given target_value. Otherwise return None if none found
    def bfs(self, target_value):
        if self.root is None:
            return None

        if self.root.get_value() == target_value:
            return self.root

        nodes_to_check = self.get_node_children(self.root)

        return self._bfs(nodes_to_check, target_value)

    def _bfs(self, nodes_to_check: 'list of Nodes', target_value):
        if len(nodes_to_check) == 0: # Failed to find target_value
            return None

        new_nodes_to_check = []
        for node in nodes_to_check: # Check nodes in next depth
            if node.get_value() == target_value:
                return node
            else:
                new_nodes_to_check.extend(self.get_node_children(node))

        return self._bfs(new_nodes_to_check, target_value)

if __name__ == "__main__":

    # Parse terminal command for values list
    parser = argparse.ArgumentParser()
    parser.add_argument('--i', )
    parser.add_argument('--values', nargs='*', type=int)
    args = parser.parse_args()

    nodes = create_nodes(args.values)

    bst = BinarySearchTree(nodes)
