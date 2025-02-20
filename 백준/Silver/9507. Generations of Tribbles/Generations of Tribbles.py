t = int(input())
fib = [1, 1, 2, 4]
for idx in range(4, 68):
    fib.append(fib[idx - 1] + fib[idx - 2] + fib[idx - 3] + fib[idx - 4])
for _ in range(t):
    n = int(input())
    print(fib[n])
        