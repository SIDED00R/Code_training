n = int(input())
ans = 1
if n == 0:
    print(ans)
else:
    for num in range(1, n + 1):
        ans *= num
    print(ans)