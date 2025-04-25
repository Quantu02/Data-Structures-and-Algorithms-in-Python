class CircularQueue:
    def __init__(self, size):
        self.queue = [None] * size
        self.max_size = size
        self.front = self.rear = -1

    def enqueue(self, data):
        if (self.rear + 1) % self.max_size == self.front:
            print("Queue is Full")
            return
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.max_size
        self.queue[self.rear] = data

    def dequeue(self):
        if self.front == -1:
            print("Queue is Empty")
            return
        data = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.max_size
        return data

    def display(self):
        if self.front == -1:
            print("Queue is Empty")
            return
        i = self.front
        while True:
            print(self.queue[i], end=" -> ")
            if i == self.rear:
                break
            i = (i + 1) % self.max_size
        print()

# Example usage:
cq = CircularQueue(5)
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.display()
cq.dequeue()
cq.display()
