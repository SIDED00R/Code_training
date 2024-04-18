E, S, M = map(int, input().split())
answer = S
E %= 15
S %= 28
M %= 19
while True:
    if answer % 15 == E and answer % 19 == M:
        break
    answer += 28
print(answer)