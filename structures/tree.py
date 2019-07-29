"""
Python implementation of a tree structure - similar to heap.
"""


class Node:
    def __init__(self, data, level, left=None, right=None):
        self.level = level
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        return str(
            {
                'level': self.level,
                'right': self.right,
                'value': self.data,
                'left': self.left,
            }
        )

    def insert(self, new_value):
        # Smaller/equal values go to the left of the node
        if new_value <= self.data:
            if not self.left:
                # New node in case of no node
                self.left = Node(new_value, self.level + 1)
                return self.left
            else:
                # Else move down the tree
                self.left.insert(new_value)
        else:
            if not self.right:
                self.right = Node(new_value, self.level + 1)
                return self.right
            else:
                self.right.insert(new_value)

    def match(self, value):
        if value == self.data:
            return self
        elif value < self.data:
            return self.left.match(value)
        elif value > self.data:
            return self.right.match(value)
        else:
            raise ValueError("Couldn't find node.")


class BinarySearchTree:
    def __init__(self, root=None):
        self.nodes = [Node(root, 1)] if root else []

    def insert_node(self, value):
        if not self.nodes:
            self.nodes = [Node(value, 1)]
        else:
            self.nodes.append(self.nodes[0].insert(value))

    def find_node(self, value):
        if not self.nodes:
            raise ValueError('No nodes to search.')
        else:
            return self.nodes[0].match(value)

    def print_all(self):
        if not self.nodes:
            print([])
        else:
            for i in self.nodes:
                print(i)


tree = BinarySearchTree()
tree.print_all() # []

tree.insert_node(10)
tree.insert_node(13)
tree.insert_node(1)
tree.insert_node(5)
tree.print_all()

tree.find_node(1)
