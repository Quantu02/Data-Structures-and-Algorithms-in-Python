stack = []

def push(data):
    stack.append(data)

def pop():
    if not stack:
        print("Stack is empty")
        return None
    return stack.pop()

def peek():
    if not stack:
        return None
    return stack[-1]

def display():
    print(stack)

# Example usage:
push(10)
push(20)
display()
print("Popped:", pop())
display()
