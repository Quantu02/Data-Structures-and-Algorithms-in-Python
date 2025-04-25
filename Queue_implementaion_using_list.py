class queue :
    def __init__(self,max_size=5):
        self.queue=[]
        self.max_size=max_size
    def eneque(self,element):
        if len(self.queue)>=self.max_size:
            print("queue is full !!  please resize or remove element..")
        else:
            self.queue.append(element)
    def dequeue(self):
        if self.queue:
            print(f"popped element is {self.queue.pop(0)} .")
        else:
            print("Queue is empty !! can't dequeue")
    def peek(self):
        if self.queue:
            print(f"First element is {self.queue[0]}")
        else:
            print("Queue is empty !!")
    def display(self):
        if self.queue:
            print(f""" elements : {self.queue}""")
        else:
            print("Queue is empty !!")
    def resize_queue(self,new_size):
        if new_size<self.max_size:
            print(f"new size must be greater than the previos size ({self.max_size})") 
        else:
            self.max_size=new_size
            print(f"queue resized to {self.max_size}")
def menu():
    q=queue()
    while True:
        choice=input("""
                    enter your choice 
                    1. Enqueue
                    2. Dequeue
                    3. Display
                    4. Peek
                    5. Resize Queue
                    6. Exit
                    ::""").strip().capitalize()
    
        match choice:
            case "1" | "Enqueue":
                element=input("enter element:")
                q.eneque(element)
            case "2" | "Dequeue":
                q.dequeue()
            case "3" | "Display":
                q.display()
            case "4" | "Peek":
                q.peek()
            case "5" | "Resize Queue":
                new_size=int(input("Enter new size:"))
                q.resize_queue(new_size)
            case "6" | "Exit" :
                print("exit")
                raise SystemExit
            case _:
                print("Invalid input!!")
if __name__=="__main__":
    menu()


    