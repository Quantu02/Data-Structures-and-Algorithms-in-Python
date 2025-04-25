def evaluate_postfix(expression):
    stack = []
    
    for token in expression.split():#['3', '4', '+', '2', '*', '7', '/']
        if token.isdigit():#checking for digit
            stack.append(int(token))#[3,4]
        else:
            operand2 = stack.pop()#4
            operand1 = stack.pop()#3
            
            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                result = operand1 / operand2 
            else:
                raise ValueError(f"Unsupported operator: {token}")
            
            stack.append(result)
    
    return stack.pop()

# Example usage
expression = "3 4 + 2 * 7 /"
print("Result:", evaluate_postfix(expression))
