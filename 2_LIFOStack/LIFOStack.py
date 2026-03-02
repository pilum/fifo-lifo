from collections import deque

class LIFOStack:
    def __init__(self):
        """Initialize an empty stack"""
        self.stack = deque([])
    
    def push(self, item):
        """Add an item to the top of the stack"""
        self.stack.append(item)
    
    def pop(self):
        """Remove and return the item from the top of the stack.
        Returns None if stack is empty."""
        return None if len(self.stack) == 0 else self.stack.pop()
    
    def peek(self):
        """Return the item at the top without removing it.
        Returns None if stack is empty."""
        return None if len(self.stack) == 0 else self.stack[-1]
    
    def is_empty(self):
        """Return True if stack is empty, False otherwise"""
        return len(self.stack) == 0
    
    def size(self):
        """Return the number of items in the stack"""
        return len(self.stack)