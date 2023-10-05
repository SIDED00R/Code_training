import itertools

def isprime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    numbers = list(numbers)
    case = []
    for i in range(1, len(numbers) + 1):
        case += list(map("".join, itertools.permutations(numbers, i)))
        
    answer = set()
    for num in case:
        num = int(num)
        if num == 1 or num == 0:
            continue
            
        if isprime(num):
            answer.add(num)
            
    
    return len(answer)