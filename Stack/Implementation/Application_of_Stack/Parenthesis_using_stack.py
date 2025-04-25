def is_balanced(expression):
    stack=[]
    brackets={")":"(","]":"[","}":"{"}
    for char in expression:
        if char in brackets.values():#opening brackets
            stack.append(char)#pushing opening bracket
        elif char in brackets.keys():#closing brackets
            if not stack or stack.pop()!=brackets[char]:
                return False
    return len(stack)==0#True if brackets are balanced
##expr1="{[]()}"
expr1=input("enter expression:")
print(f"checking expression {expr1} : {is_balanced(expr1)}")
