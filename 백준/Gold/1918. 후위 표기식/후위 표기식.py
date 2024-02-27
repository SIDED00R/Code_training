def shunting_yard(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    output_queue = []
    operator_stack = []
    
    for token in expression:
        if token.isalpha(): 
            output_queue.append(token)
        elif token in precedence:  
            while (operator_stack and operator_stack[-1] in precedence and
                   precedence[operator_stack[-1]] >= precedence[token]):
                output_queue.append(operator_stack.pop())
            operator_stack.append(token)
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':  
            while operator_stack[-1] != '(':
                output_queue.append(operator_stack.pop())
            operator_stack.pop() 
    
    while operator_stack:
        output_queue.append(operator_stack.pop())
    
    return ''.join(output_queue)

expression = input()
print(shunting_yard(expression))