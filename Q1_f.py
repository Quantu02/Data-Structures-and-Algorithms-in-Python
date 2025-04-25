class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class SLL:
    def __init__(self,start=None):
        self.start=start
    def is_empty(self):
        return self.start == None
    def insert_at_first(self,data):
        n=Node(data,self.start)
        self.start=n
    def ith_position(self,temp,data):
        if temp is not None:
            n=Node(data,temp.next)
    def delete_first(self):
        if self.start is not None:
            self.start=self.start.next
    def search(self,data):
        temp=self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp=temp.next
        return None 

    def ith_positon(self,data):
        if self.start is  None:
            pass
        elif self.start.next is None:
            if self.start.item == data:
                self.start=None
        else:
            temp=self.start
            if temp.item == data:
                self.start = temp.next
            else:
                while temp.next is not None:
                    if temp.next.item == data:
                        temp.next = temp.next.next
                        break
                    temp=temp.next
    def print_list(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end='')
            temp=temp.next
