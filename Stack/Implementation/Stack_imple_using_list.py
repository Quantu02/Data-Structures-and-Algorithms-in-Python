class stack:
    def __init__(self):
        self.list=[]
    def __len__(self):
        return  len(self.list)
    def __is_empty__(self):
        return len(self.list)==0
    def push(self,element):
        self.list.append(element)
    def pop(self):
        if self.__is_empty__():
            print("Underflow")
        else:
            return self.list.pop()
    def peek(self):
        if  self.__is_empty__():
            print("list is empty")
        else:
            return self.list[-1]
array=stack()
while True:
    inp=input("""
    1.push
    2.pop
    3.peek
    4.view list
    5.Exit
    ::""")
    match inp:
        case "1" | "push":
            element=input("enter element:")
            array.push(element)
        case "2" | "pop":
            print(f"popped element is {array.pop()}")
        case "3" | "peek":
            print(f"peek element of stack is {array.peek()}")
        case "4" | "view list":
            print(array.list)
        case "5" | "Exit" :
            print("exit")
            raise SystemExit
