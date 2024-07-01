def gcd(a, b):
    while b != 0:
        a, b= b, a % b
    return a

a, b = map(int, input().split())
epsilon = a / b
x, c = map(int, input().split())
x0 = int(input())
l = x * x0 + c
print(l)
if x == 0:
    print(0, 0)
else:
    first = a
    second = b * abs(x)
    g = gcd(first, second)
    first //= g
    second //= g
    if first > 1e8 or second > 1e8:
        print(0, 0)
    else:
        print(first, second)
    
