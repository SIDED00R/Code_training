from collections import deque

def solution(prices):
    prices = deque(prices)
    answer = [0 for _ in range(len(prices))]
    stack = [[prices.popleft(), 0]]
    idx = 0
    for i in range(len(prices) - 1):
        price = prices.popleft()
        idx += 1
        
        while stack and price < stack[-1][0]:
            p, i = stack.pop()
            answer[i] = idx - i
        stack.append([price, idx])
        
    while stack:
        p, i = stack.pop()
        answer[i] = len(answer) - 1 - i
    
    return answer
    