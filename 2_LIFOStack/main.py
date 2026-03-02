from LIFOStack import LIFOStack

# Test cases
stack = LIFOStack()
print(stack.is_empty())  # Should print: True

stack.push("X")
stack.push("Y")
stack.push("Z")
print(stack.size())      # Should print: 3
print(stack.peek())      # Should print: Z

print(stack.pop())       # Should print: Z
print(stack.pop())       # Should print: Y
print(stack.size())      # Should print: 1
print(stack.peek())      # Should print: X