import math

def find(num):
    answer = 0
    for i in [2, 3, 5, 7, 11, 13, 17]:
        answer += math.comb(18, i) * ((100 - num) ** (18 - i)) * (num ** i) / (100 ** 18)
    return answer
a = int(input())
b = int(input())

print( 1 - (1 - find(a)) * (1 - find(b)))