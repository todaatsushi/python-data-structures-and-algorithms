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
        return (index - 1 ) / 2 if index != 0 else None

    def get_min(self):
        """
        Returns the smallest (first) item in heap.
        """
        if len(self.nodes) == 0:
            raise IndexError('Heap is empty!')
        return self.nodes.pop(0)

    def add_node(self, node):
        self.nodes.append(node)

    def swap_nodes(self, n1_index, n2_index):
        """
        Takes heap array and 2 Node instances and swaps the position of the 2 nodes,
        returning the newly organised heap array.
        """
        n1 = self.nodes[n1_index]
        n2 = self.nodes[n2_index]

        self.nodes[n1_index] = n2
        self.nodes[n2_index] = n1

    def adjust_heap_up(self):
        """
        Gets the last item in the heap and bubbles it up to its correct position.
        """

        # Current node
        val = self.nodes[len(self.nodes) - 1]
        index = self.nodes.index(val) # Starts as last node

        # Parent node
        p_index = self.get_parent_index(index)
        p_val = self.nodes[p_index]
        
        while p_index and p_val > val:
            self.swap_nodes(index, p_index)
            val = p_val
            index = p_index
            p_index = self.get_parent_index(index)
            p_val = self.nodes[p_index]

    def adjust_heap_down(self):
        """
        Takes the smallest value and bubbles it down to the correct position
        """
        index = 0
        children = self.get_child_indicies(index)
