n = int(input())
answer = 0
for _ in range(n):
    if sum(map(int, input().split())) >= 2:
        answer += 1
print(answer)