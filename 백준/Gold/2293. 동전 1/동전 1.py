import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
    
coins = sorted(coins)
cases = [0] * (k + 1)
cases[0] = 1

for coin in coins:
    for price in range(coin, k + 1):
        cases[price] += cases[price - coin]
        
print(cases[-1])