def defcimal_to_binary(decimal_num):
    #5=001
    stack=[]
    if decimal_num==0:
        return "0"
    while decimal_num>0:
        remainder=decimal_num%2
        stack.append(remainder)
        decimal_num//=2
    binary_num=""
    while stack:
        binary_num+=str(stack.pop())
    return binary_num
n=4
print(defcimal_to_binary(n))
n=5
print(defcimal_to_binary(n))
n=6
print(defcimal_to_binary(n))
n=7
print(defcimal_to_binary(n))
n=8
print(defcimal_to_binary(n))
n=9
print(defcimal_to_binary(n))
n=10
print(defcimal_to_binary(n))


