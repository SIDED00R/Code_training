def first(num):
    str_num = str(num)
    total = 0
    for d in str_num:
        total += int(d)
    if total % 2 == 0:
        return False
    else:
        return True

def second(num):
    if num == 1:
        return False
    prime = set()
    for p in range(2, int(num ** 0.5) + 1):
        while num % p == 0:
            num //= p
            prime.add(p)
    if num != 1:
        prime.add(num)
    if len(prime) % 2 == 0:
        return True
    else:
        return False
    
n = int(input())

f = False
s = False
if (n >= 6 or n == 4) and first(n):
    f = True

if n in [2, 4] or second(n):
    s = True

if f and s:
    print(4)
elif f:
    print(1)
elif s:
    print(2)
else:
    print(3)