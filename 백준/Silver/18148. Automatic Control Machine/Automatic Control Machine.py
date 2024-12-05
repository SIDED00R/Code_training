t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    total = []
    answer = 50
    for _ in range(m):
        total.append(int(input(), 2))
    for i in range(1 << m):
        binary = f"{i:0{m}b}"
        ans = 0
        count = 0
        for j in range(m):
            if binary[j] == "1":
                count += 1
                ans = total[j] | ans
        if ans == 2 ** n - 1:
            answer = min(answer, count)
    if answer == 50:
        print(-1)
    else:
        print(answer)


    