def solution(n):
    
    answer = 0
    
    for i in range(1, n + 1):
        total = i
        while total < n:
            i += 1
            total += i
        if total == n:
            answer += 1
        
    return answer

