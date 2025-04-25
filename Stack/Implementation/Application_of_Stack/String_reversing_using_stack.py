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
    def reverse_str(self,string):
        rev_list=[]
        reverse_string=""
        for i in range(len(string)):
           rev_list.append(string[i])#push
        for j in range (len(string)):
            reverse_string+=rev_list.pop()
        return reverse_string
array=stack()
while True:
    inp=input("""
    1.push
    2.pop
    3.peek
    4.display
    5.reversing of string
    6.Exit
    ::""")
    match inp:
        case "1" | "push":
            element=input("enter string:")
            array.push(element)
        case "2" | "pop":
            print(f"popped element is {array.pop()}")
        case "3" | "peek":
            print(f"peek element of stack is {array.peek()}")
        case "4" | "display":
            print(array.list)
        case "5" | "reversing of string": 
            if array.__is_empty__():
                print("Stack is empty!!,enter any element for reversing..")
            else:
                print("stack element:")
                for i,element in enumerate(array.list):
                    print(f"{i+1}. {element}")
                string=input("choose any string:")
                print(f"reverse string is {array.reverse_str(array.list[int(string)-1])}")    
        case "6" | "Exit" :
            print("exit") 
            raise SystemExit
