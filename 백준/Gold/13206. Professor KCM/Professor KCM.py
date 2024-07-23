import sys
import math

def lcm(a, b):
    answer = a * b // math.gcd(a, b)
    return answer
    
t = int(input())
for _ in range(t):
    n = int(input())
    line = list(map(int, sys.stdin.readline().split()))
    answer = line[0]
    for num in line[1:]:
        answer = lcm(answer, num)  
    print(answer % 1000000007)