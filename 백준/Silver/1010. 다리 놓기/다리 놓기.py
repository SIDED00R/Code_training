import math
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(math.comb(k, n))