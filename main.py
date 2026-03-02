from FIFOQueue import FIFOQueue

###############################################
# Testing: Excercise 1.

queue = FIFOQueue()
print(queue.is_empty())  # Should print: True

queue.enqueue("A")
queue.enqueue("B")
queue.enqueue("C")
print(queue.size())      # Should print: 3
print(queue.peek())      # Should print: A
print(queue.dequeue())   # Should print: A
print(queue.dequeue())   # Should print: B
print(queue.size())      # Should print: 1
print(queue.peek())      # Should print: C
###############################################