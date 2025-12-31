n, m = map(int, input().split())
if n % 2 == 0:
    print(m * n)
    for i in range(n):
        for j in range(1, m):
            if i % 2 == 0:
                print(i + 1, j + 1)
            else:
                print(i + 1, m - j + 1)
    for i in range(n):
        print(n - i, 1)
elif m % 2 == 0:
    print(n * m)
    for j in range(m):
        for i in range(1, n):
            if j % 2 == 0:
                print(i + 1, j + 1)
            else:
                print(n - i + 1, j + 1)
    for j in range(m):
        print(1, m - j)
    
else:
    print(n * m - 1)
    for i in range(1, n):
        print(i + 1, 1)
    for i in range(n, 2, -1):
        for j in range(2):
            if i % 2 == 0:
                print(i, 3 - j)
            else:
                print(i, 2 + j)
    print(2, 3)
    for j in range(3, m):
        for i in range(1, n):
            if j % 2 == 1:
                print(i + 1, j + 1)
            else:
                print(n - i + 1, j + 1)
    for j in range(m):
        print(1, m - j)
            
            