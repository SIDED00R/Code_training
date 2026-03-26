n = int(input())
stack = []
if n == 1:
    print(3)
    print(1, 1)
    print(2, 1)
    print(1, 1)
else:
    print(n * (n + 2))
    for i in range(1, 2 * n + 2):
        if i <= n:
            for j in range(i):
                print(i % 2 + 1, j + 1)
        elif i == n + 1:
            for j in range(n):
                print(i % 2 + 1, j + 1)
        else:
            for j in range(i - n - 2, n):
                print(i % 2 + 1, j + 1)
            
    