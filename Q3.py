class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_front(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new_node
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, key, data):
        temp = self.head
        while True:
            if temp.data == key:
                new_node = Node(data)
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next
            if temp == self.head:
                break
        print(f"{key} not found.")

    def insert_back(self, data):
        if not self.head:
            self.insert_front(data)
            return
        new_node = Node(data)
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new_node
        new_node.next = self.head

    def remove_back(self):
        if not self.head:
            print("List is empty")
            return
        temp = self.head
        if temp.next == self.head:
            self.head = None
            return
        while temp.next.next != self.head:
            temp = temp.next
        temp.next = self.head

    def remove_front(self):
        if not self.head:
            print("List is empty")
            return
        temp = self.head
        if temp.next == self.head:
            self.head = None
            return
        last = self.head
        while last.next != self.head:
            last = last.next
        self.head = self.head.next
        last.next = self.head

    def remove_element(self, key):
        if not self.head:
            return
        temp = self.head
        prev = None
        while True:
            if temp.data == key:
                if prev:
                    prev.next = temp.next
                else:
                    self.remove_front()
                return
            prev = temp
            temp = temp.next
            if temp == self.head:
                break
        print(f"{key} not found.")

    def search(self, key):
        temp = self.head
        while True:
            if temp.data == key:
                return temp
            temp = temp.next
            if temp == self.head:
                break
        return None

    def display(self):
        if not self.head:
            print("List is empty")
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(back to head)")

# Example usage:
cll = CircularLinkedList()
cll.insert_back(1)
cll.insert_back(2)
cll.insert_back(3)
cll.insert_front(0)
cll.insert_after(2, 2.5)
cll.display()

cll.remove_element(2)
cll.display()

node = cll.search(2.5)
print(f"Found: {node.data}" if node else "Not found")
