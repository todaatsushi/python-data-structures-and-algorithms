"""
Python implementation of stack.
"""

class Stack:
    def __init__(self):
        self.vals = []

    def put(self, new):
        return self.vals.append(new)

    def get(self):
        return self.vals.pop()

    def __str__(self):
        return str(self.vals)


stack = Stack()
print(stack) # []

stack.put(1)
stack.put(5)

print(stack) # [1, 5]

print(stack.get()) # 5

print(stack) # [1]
