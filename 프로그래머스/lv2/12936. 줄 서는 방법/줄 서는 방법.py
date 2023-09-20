def solution(n, k):
    k -= 1
    people = [i for i in range(1, n + 1)]
    factorial = []
    answer = []
    
    fact = 1
    for num in range(1, n):
        fact *= num
        factorial.append(fact)
        
    for i in range(n - 1):
        lastnum = factorial.pop()
        count = k // lastnum
        k %= lastnum
        answer.append(people.pop(count))
    answer.append(people.pop())    
    return answer