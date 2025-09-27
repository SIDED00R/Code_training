n = int(input())
line = list(input().split())
answer = 0
for num in line:
    if int(num[-1]) == n:
        answer += 1
print(answer)