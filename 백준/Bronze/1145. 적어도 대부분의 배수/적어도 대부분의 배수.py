from itertools import combinations
import math

def lcm(a, b):
    return a * b // math.gcd(a, b)

def find(now_case):
    return lcm(lcm(now_case[0], now_case[1]), now_case[2])

l = list(map(int, input().split()))
answer = 1e10
for now_case in combinations(l, 3):
    answer = min(find(now_case), answer)
print(answer)