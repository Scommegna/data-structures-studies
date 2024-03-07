"""
Add a method to push a value onto the Stack implementation that we began in the last Coding Exercise.

Remember: This Stack implementation uses a list instead of a linked list.
"""

class Stack:
    def __init__(self):
        self.stack_list = []
        
    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def push(self, value):
        self.stack_list.append(value)
    