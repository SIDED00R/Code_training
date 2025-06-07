def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

n, k = map(int, input().split())
v = []

while k > 2:
    n -= 2
    v.append(2)
    k -= 1

if n % 2 and v:
    v[-1] += 1
    n -= 1

if k == 1 and not is_prime(n):
    print(-1)
elif k == 1:
    print(n)
elif n < 4:
    print(-1)
elif is_prime(n - 2):
    for num in v:
        print(num, end=' ')
    print(2, n - 2)
elif n % 2:
    print(-1)
else:
    x = 3
    while True:
        if is_prime(x) and is_prime(n - x):
            for num in v:
                print(num, end=' ')
            print(x, n - x)
            break
        x += 2
