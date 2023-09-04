def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def solution(a, b):
    
    num = gcd(max(a, b), min(a, b))
    a, b = a // num, b // num
    while b != 1:
        if b % 2 == 0:
            b //= 2
            print(b)
        elif b % 5 == 0:
            b //= 5
            print(22)
        else:
            return 2
            
        print(b, 1)
    return 1