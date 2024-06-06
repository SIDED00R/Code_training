import math
n = int(input())
cows = []
for _ in range(n):
    cows.append(int(input()))
    
answer = math.inf

for i in range(n):
    total = 0
    for j in range(n):
        total += cows[(j + i) % n] * j
    answer = min(answer, total)
    
print(answer)