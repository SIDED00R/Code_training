p, n = map(int, input().split())
line = sorted(list(map(int, input().split())))
answer = 0
for w in line:
    if p < 200:
        answer += 1
        p += w
print(answer)
