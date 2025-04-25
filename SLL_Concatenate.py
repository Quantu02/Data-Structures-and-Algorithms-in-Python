class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=' -> ')
            temp = temp.next
        print("None")

    def concatenate(self, other):
        if not self.head:
            self.head = other.head
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = other.head


# First list
list1 = LinkedList()
list1.append(1)
list1.append(2)
list1.append(3)

# Second list
list2 = LinkedList()
list2.append(4)
list2.append(5)

# Concatenate
list1.concatenate(list2)

# Display result
list1.display()
