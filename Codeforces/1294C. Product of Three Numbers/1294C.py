def find(start, num):
    for q in range(start, int(num ** 0.5) + 1):
        if num % q == 0:
            return num // q, q
    return num, 1

n = int(input())
for _ in range(n):
    num = int(input())
    left_num, a = find(2, num)
    if a == 1:
        print("NO")
        continue
    else:
        c, b = find(a + 1, left_num)
        if b == 1 or b == c:
            print("NO")
        else:
            print("YES")
            print(a, b, c)