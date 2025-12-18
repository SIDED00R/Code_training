letter = input()
n = int(input())
answer = 0
for _ in range(n):
    line = input()
    if letter in line * 2:
        answer += 1

print(answer)