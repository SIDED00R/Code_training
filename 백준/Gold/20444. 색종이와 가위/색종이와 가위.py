n, k = map(int, input().split())
test = n ** 2 - 4 * (k - n - 1)
if test >= 0 and int(test ** 0.5) ** 2 == test and (n + test ** 0.5) % 2 == 0 and n - test ** 0.5 >= 0:
    print("YES")
else:
    print("NO")