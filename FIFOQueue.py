from collections import deque

class FIFOQueue:
    def __init__(self):
        """Initialize an empty queue"""
        self.queue = deque([])

    def enqueue(self, item):
        """Add an item to the back of the queue"""
        self.queue.append(item)
    
    def dequeue(self):
        """Remove and return the item from the front of the queue.
        Returns None if queue is empty."""
        return None if len(self.queue) == 0 else self.queue.popleft()
    
    def peek(self):
        """Return the item at the front without removing it.
         Returns None if queue is empty."""
        return None if len(self.queue) == 0 else self.queue[0]
    
    def is_empty(self):
        """Return True if queue is empty, False otherwise"""
        return len(self.queue) == 0
    
    def size(self):
        """Return the number of items in the queue"""
        return len(self.queue)