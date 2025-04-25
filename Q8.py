class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularQueueLL:
    def __init__(self):
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if not self.rear:
            self.rear = new_node
            self.rear.next = new_node
        else:
            new_node.next = self.rear.next
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if not self.rear:
            print("Queue is Empty")
            return None
        front = self.rear.next
        if self.rear == front:
            self.rear = None
        else:
            self.rear.next = front.next
        return front.data

    def display(self):
        if not self.rear:
            print("Queue is Empty")
            return
        temp = self.rear.next
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.rear.next:
                break
        print()

# Example usage:
cql = CircularQueueLL()
cql.enqueue(10)
cql.enqueue(20)
cql.enqueue(30)
cql.display()
cql.dequeue()
cql.display()
