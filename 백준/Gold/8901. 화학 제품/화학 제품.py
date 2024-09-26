n = int(input())
for _ in range(n):
    a, b, c = map(int, input().split())
    ab, bc, ca = map(int, input().split())
    answer = 0
    for i in range(min(a, b) + 1):
        now_ab = ab * i
        for j in range(min(b - i, c) + 1):
            now = now_ab + bc * j
            now += ca * min(c - j, a - i)
            answer = max(answer, now)
    print(answer)
        
    