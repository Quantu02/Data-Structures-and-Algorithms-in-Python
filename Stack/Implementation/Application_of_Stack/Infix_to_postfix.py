def precedence(op):
    if op == '^':
        return 3
    elif op in ('*', '/', '%'):
        return 2
    elif op in ('+', '-'):
        return 1
    return 0

def infix_to_postfix(expression):
    stack = []
    output = []
    for token in expression:
        if token.isalnum():  # Operand
            output.append(token)
        elif token == '(':  # Left Parenthesis
            stack.append(token)
        elif token == ')':  # Right Parenthesis
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Remove '('
        else:  # Operator
            while stack and precedence(stack[-1]) >= precedence(token):
                output.append(stack.pop())
            stack.append(token)

    while stack:
        output.append(stack.pop())

    return " ".join(output)

# Example Usage
expr = "( A + B ) * C"
expr = expr.replace(" ", "")  # Remove spaces
print(infix_to_postfix(expr))  # Output: A B + C *
