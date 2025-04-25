class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        tail = self.head
        while tail.next:
            tail = tail.next
        tail.next = new_node
        new_node.prev = tail

    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end=" <-> ")
            curr = curr.next
        print("None")

def concatenate(list1, list2):
    if not list1.head:
        list1.head = list2.head
        return
    if not list2.head:
        return
    # Find tail of first list
    tail1 = list1.head
    while tail1.next:
        tail1 = tail1.next
    # Connect tail of list1 to head of list2
    tail1.next = list2.head
    list2.head.prev = tail1


dll1 = DoublyLinkedList()
dll1.append(1)
dll1.append(2)

dll2 = DoublyLinkedList()
dll2.append(3)
dll2.append(4)

concatenate(dll1, dll2)
dll1.display()
