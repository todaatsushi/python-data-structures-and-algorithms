"""
Python implementation of the heap (min heap) data structure.
"""


class MinHeap:
    def __init__(self):
        self.nodes = []

    def get_child_indicies(self, index):
        """
        Given its own index in the heap, returns the node's children's indicies.
        """
        left = 2 * index + 1
        right = 2 * index + 2

        # Make sure indicies are valid
        # Left
        try:
            self.nodes[left]
        except IndexError:
            left = None
            print('No left child node')
        
        # Right
        try:
            self.nodes[right]
        except IndexError:
            right = None
            print('No right child node')
        
        # Validation
        if not right and not left:
            raise IndexError("Node has no children")  

        return {
            'left': left,
            'right': right,
        }

    def get_parent_index(self, index):
        if index == 0:
            raise IndexError('Min value, no parent')
        else:
            return (index - 1 ) / 2

    def get_min(self):
        """
        Returns the smallest (first) item in heap.
        """
        if len(self.nodes) == 0:
            raise IndexError('Heap is empty!')
        return self.nodes.pop(0)

    def add_node(self, node):
        self.nodes.append(node)

    def swap_nodes(self, node1, node2):
        """
        Takes heap array and 2 Node instances and swaps the position of the 2 nodes,
        returning the newly organised heap array.
        """
        # Get indicies
        n1_index = self.nodes.index(node1)
        n2_index = self.nodes.index(node2)

        # Swap
        self.nodes[n1_index] = node2
        self.nodes[n2_index] = node1

    # def adjust_heap_up(self):
    #     """
    #     Gets the last item in the heap and bubbles it to its correct position.
    #     """
    #     val = self.nodes[len(self.nodes) - 1]
    #     index = self.nodes.index(val) # should be len(self.nodes)
        
    #     while self.get_parent_index()

