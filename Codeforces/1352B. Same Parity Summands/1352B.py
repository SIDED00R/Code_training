t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    find = True
    if n >= k and (n - k) % 2 == 0:
        answer = ["1"] * k
        answer[0] = str(n - k + 1)
    elif n >= 2 * k and n % 2 == 0:
        answer = ["2"] * k
        answer[0] = str(n - 2 * k + 2)
    else:
        find = False
    if find:
        print("YES")
        print(" ".join(answer))
    else:
        print("NO")