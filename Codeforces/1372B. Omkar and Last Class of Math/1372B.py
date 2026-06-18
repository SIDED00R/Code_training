def p(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return i
    return 1
t = int(input())
for _ in range(t):
    n =int(input())
    prime = p(n)
    if prime == 1:
        print(1, n - 1)
    else:
        print(n // prime, n - n // prime)