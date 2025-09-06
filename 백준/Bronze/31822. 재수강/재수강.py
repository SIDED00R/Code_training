code = input()[:5]
n = int(input())
answer = 0
for _ in range(n):
    name = input()[:5]
    if code == name:
        answer += 1

print(answer)