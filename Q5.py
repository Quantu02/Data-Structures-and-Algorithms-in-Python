class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackLL:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.top:
            print("Stack is empty")
            return None
        popped = self.top.data
        self.top = self.top.next
        return popped

    def peek(self):
        if not self.top:
            return None
        return self.top.data

    def display(self):
        temp = self.top
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Example usage:
stack = StackLL()
stack.push(10)
stack.push(20)
stack.display()
print("Popped:", stack.pop())
stack.display()
