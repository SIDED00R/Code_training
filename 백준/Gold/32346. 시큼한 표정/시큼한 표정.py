import math

n = int(input())
line = input()
keep = []
for idx in range(n - 1):
    if line[idx] == '>' and line[idx + 1] == '<':
        keep.append(idx)

answer = 0
for now_case in keep:
    front = now_case
    back = now_case + 1
    total = n - 2
    while front >= 0 and back < n and line[front] == '>' and line[back] == '<':
        answer += math.comb(total, front)
        answer %= 1000000007
        front -= 1
        back += 1
        total -= 2
        
print(answer)
