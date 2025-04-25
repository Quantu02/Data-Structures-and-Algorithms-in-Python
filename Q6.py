def evaluate_postfix(expression):
    stack = []
    for char in expression.split():
        if char.isdigit():
            stack.append(int(char))
        else:
            b = stack.pop()
            a = stack.pop()
            if char == '+':
                stack.append(a + b)
            elif char == '-':
                stack.append(a - b)
            elif char == '*':
                stack.append(a * b)
            elif char == '/':
                stack.append(a / b)
    return stack.pop()

# Example usage:
exp = "5 6 2 + * 12 4 / -"  # ((6+2)*5)-(12/4)
print("Result:", evaluate_postfix(exp))
