a, b = map(int, input().split())
n = int(input())
l = []
for _ in range(n):
    l.append(int(input()))
    
l.sort()

low = 1001000
high = -10000

for num in l:
    if num <= b:
        low = num
    else:
        high = num
        break

answer = abs(a - b)
answer = min(answer, abs(low - b) + 1, abs(high - b) + 1)
print(answer)