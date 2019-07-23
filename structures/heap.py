"""
Python implementation of the heap (min heap) data structure.
"""


class MinHeap:
    def __init__(self, min=None):
        self.nodes = [] if not min else [min]

    def __str__(self):
        return str(self.nodes)

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
        
        # Right
        try:
            self.nodes[right]
        except IndexError:
            right = None
        
        # Validation
        if not right and not left:
            return None

        return {
            'left': left,
            'right': right,
        }

    def get_parent_index(self, index):
        """
        Gets the index of the parent node given that node's index.
        """
        return int((index - 1 ) / 2) if index != 0 else None

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
        
        while p_index is not None and p_val > val:
            self.swap_nodes(index, p_index)
            val = p_val
            index = p_index
            p_index = self.get_parent_index(index)
            
            # If unsortable, break
            if not p_index:
                break
            else:
                p_val = self.nodes[p_index]

    def adjust_heap_down(self):
        """
        Takes the smallest value and bubbles it down to the correct position
        """
        index = 0
        children = self.get_child_indicies(index)
        left = children['left']
        right = children['right']

        while left:
            if right and self.nodes[right] < self.nodes[left]:
                smaller_child_index = right
            else:
                smaller_child_index = left

            if self.nodes[index] > self.nodes[smaller_child_index]:
                self.swap_nodes(index, smaller_child_index)
            
            index = smaller_child_index
            children = self.get_child_indicies(index)

            # Check if we have reached the bottom
            if children is None:
                break

            left = children['left']
            right = children['right']

    def get_min(self):
        """
        Returns the smallest (first) item in heap, adjusts the heap down after.
        """
        if len(self.nodes) == 0:
            raise IndexError('Heap is empty!')
        
        # Remove and replace min node with last added node
        self.swap_nodes(0, len(self.nodes) - 1)
        min = self.nodes.pop()

        self.adjust_heap_down()
        return min

    def add_node(self, node):
        """
        Adds a node value to the end of the heap, adjusts it up.
        """
        self.nodes.append(node)

        self.adjust_heap_up()


# Initialising the heap
heap = MinHeap(10)
heap2 = MinHeap()

# print(heap, heap2) # [10], []

# Add value to heap
heap.add_node(1) # Smaller value
heap.add_node(13)

print(heap) # [1, 10, 13]

# More values
for i in [5, 14, 2]:
    heap.add_node(i)

print(heap) # [1, 5, 2, 10, 14, 13]


# Pop values
print(heap.get_min()) # 1
print(heap) # [2, 5, 13, 10, 14]
