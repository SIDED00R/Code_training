import math

t = int(input())
for _ in range(t):
    n = int(input())
    if n % 2 == 1:
        print("Bob")
    else:
        if 2 ** int(math.log2(n)) == n:
            if int(math.log2(n)) % 2 == 1:
                print("Bob")
            else:
                print("Alice")
        else:
            print("Alice")