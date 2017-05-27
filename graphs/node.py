# import pdb

class Node:
    def __init__(self, value, parent=None, left=None, right=None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

    def get_value(self):
        return self.value

    def set_value(self, new_value):
        self.value = new_value

    def get_parent(self):
        return self.parent

    def set_parent(self, new_parent):
        self.parent = new_parent

    def get_left(self):
        return self.left

    def has_left(self):
        return not self.left is None

    def set_left(self, new_left):
        self.left = new_left

    def get_right(self):
        return self.right

    def has_right(self):
        return not self.right is None

    def set_right(self, new_right):
        self.right = new_right

    def __str__(self):
        return "Value: " + str(self.get_value()) + " Parent: " + str(self.parent) + " Left: " + str(self.left) + " Right: " + str(self.right)

def create_nodes(values):
    nodes = []
    for value in values:
        nodes.append(Node(value))

    return nodes
