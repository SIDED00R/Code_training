def solution(prices):
    answer = [0 for _ in range(len(prices))]
    stack = []
    
    for i in range(len(prices)):
        price = prices[i]
        
        while stack and price < stack[-1][0]:
            p, idx = stack.pop()
            answer[idx] = i - idx
        stack.append([price, i])
        
    while stack:
        p, i = stack.pop()
        answer[i] = len(answer) - 1 - i
    
    return answer
    