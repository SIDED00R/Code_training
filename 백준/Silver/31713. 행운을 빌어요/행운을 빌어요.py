
t = int(input())

def check(a, b):
    if a * 3 >= b:
        return a * 3 - b
    elif a * 4 >= b:
        return 0
    else:
        return check(a + 1, b) + 1
    
for _ in range(t):
    a, b = map(int, input().split())
    print(check(a, b))
        