"""
Python implementation of heap.
"""

class Heap:
    def __init__(self):
        self.vals = []

    def put(self, new):
        return self.vals.append(new)

    def get(self):
        return self.vals.pop()

    def __str__(self):
        return str(self.vals)


heap = Heap()
print(heap) # []

heap.put(1)
heap.put(5)

print(heap) # [1, 5]

print(heap.get()) # 5

print(heap) # [1]
