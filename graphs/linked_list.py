from node import Node
import argparse

class LinkedList:
    # Create linked list from given values and return root
    def __init__(self, values):
        prev_node = None

        # Create a linked list of length LIST_LENGTH
        for value in values:
            new_node = Node(value)

            if not prev_node is None: # Doubley link next node
                prev_node.set_left(new_node)
                new_node.set_parent(prev_node)
            else: # set root
                self.root = new_node

            prev_node = new_node

    def get_root(self):
        return self.root

    def __str__(self):
        is_tail = False
        cur_node = self.root
        contents = ""
        print("List contents from head to tail:")

        while not is_tail:
            # pdb.set_trace()
            contents += str(cur_node.get_value()) + " "
            if not cur_node.has_left():
                is_tail = True
            else:
                cur_node = cur_node.get_left()

        return contents

if __name__ == "__main__":
    # Parse terminal command for values list
    parser = argparse.ArgumentParser()
    parser.add_argument('--values', nargs='*')
    args = parser.parse_args()

    ll = LinkedList(args.values)
