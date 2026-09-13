"""Program 3.2: stack using a list."""
stack = []
def push(item): stack.append(item)
def pop(): return stack.pop() if stack else "Stack is empty"
def peek(): return stack[-1] if stack else "Stack is empty"
def is_empty(): return not stack
def display(): print("Stack:", stack)

for item in [10, 20, 30, 40, 50]: push(item)
display()
print("Peek:", peek())
print("Popped:", pop(), pop())
display()
print("Is empty:", is_empty())
