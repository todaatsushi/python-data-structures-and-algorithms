"""
Python implementation of a queue data structure.
"""


class Queue:
    def __init__(self, *args):
        self.vals = [val for val in args]
    def __str__(self):
        return str(self.vals)

    def add(self, value):
        return self.vals.append(value)

    def remove(self):
        try:
            return self.vals.pop(0)
        except IndexError:
            raise IndexError('Queue is empty.')


q = Queue()
print(q) # []

q.add(0)
q.add(4)
q.add(8)
print(q) # [0, 4, 8]

print(q.remove()) # 0
print(q) # [4, 8]

q0 = Queue(0, 4, 6, 8)
print(q0)

q2 = Queue()
q2.remove()

