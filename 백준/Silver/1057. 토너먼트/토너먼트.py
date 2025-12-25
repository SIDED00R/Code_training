n, a, b = map(int, input().split())
a, b = min(a, b), max(a, b)
answer = 0
while True:
    answer += 1
    if a + 1 == b and a % 2 == 1:
        print(answer)
        break
    else:
        a = (a + 1) // 2
        b = (b + 1) // 2