"""
Python implementation of linked list.
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def link_node(self, node):
        self.next = node


class SinglyLinkedList:
    def __init__(self, first_node=None):
        self.first_node = first_node

    def search(self, value):
        node = self.first_node

        while True:
            if node.value == value:
                return node
            elif node.next == None:
                raise IndexError('Value does not exist in linked list.')
            
            node = node.next

    def __str__(self):
        vals = []
        node = self.first_node

        while node is not None:
            vals.append(node.value)
            node = node.next

        return str(vals)
        


# Initialising list
n1 = Node(13)
single_linked_list = SinglyLinkedList(n1)
print(single_linked_list.first_node.value) # 13

# Adding nodes
n2 = Node(1)
n3 = Node(45)

single_linked_list.first_node.link_node(n2) # 13, 1
single_linked_list.first_node.next.link_node(n3) # 13, 1, 45
print(single_linked_list)

# Finding nodes
print(single_linked_list.search(1)) # Returns second node

try:
    single_linked_list.search(46) # Raise IndexError
except IndexError:
    print("IndexError as expected.")



# Doubly linked list
class dNode:
    def __init__(self, value, previous=None, next=None):
        self.value = value
        self.previous = previous
        self.next = next
    
    def link_previous(self, node):
        self.previous = node
        node.next = self
    
    def link_next(self, node):
        self.next = node
        node.previous = self


class DoublyLinkedLists(SinglyLinkedList):
    pass


# Init list
doubly_linked_list = DoublyLinkedLists()
n4 = dNode(14)
doubly_linked_list.first_node = n4

# Adding nodes
n5 = dNode(5)
n6 = dNode(7)

doubly_linked_list.first_node.link_next(n5)
doubly_linked_list.first_node.link_next(n6)
print(doubly_linked_list)

# Traversing list
print(doubly_linked_list.first_node.next.value) # 5
print(doubly_linked_list.first_node.next.previous.value) # 14

print(doubly_linked_list.search(14)) # Returns second node

try:
    doubly_linked_list.search(13) # Raises error
except IndexError:
    print("IndexError as expected.")
