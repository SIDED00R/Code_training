import copy
n, m = map(int, input().split())

if n == m:
    print('YES')
    exit()
s = set()
s.add(n)
while s:
    next_set = set()
    for num in s:
        if num % 2 == 0:
            if num // 2 == m:
                print('YES')
                exit()
            elif num // 2 > m:
                next_set.add(num // 2)
        else:
            if num // 2 == m or num // 2 + 1 == m:
                print('YES')
                exit()
            elif num // 2 > m:
                next_set.add(num // 2)
                next_set.add(num // 2 + 1)
    s = next_set.copy()
print('NO')