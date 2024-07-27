h, w = map(int, input().split())
answer = 0
for _ in range(h):
    on = False
    for case in input():
        if on:
            if case == "/" or case == "\\":
                on = False
                answer += 0.5
            else:
                answer += 1
        else:
            if case == "/" or case == "\\":
                on = True
                answer += 0.5
print(int(answer))