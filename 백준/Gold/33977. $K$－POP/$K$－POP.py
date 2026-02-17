k = int(input())

a = 0
b = k

for i in range(1, k // 2 + 2):
    if k % i == 0:
        j = k // i
        if abs(a - b) > abs(i - j):
            a = i
            b = j

leap = [i + 2 for i in range(a)]
now_b = a + 1
print(a + b)
for _ in range(b - 1):
    now_b += 1
    front = leap.pop()
    print(front, now_b)
    if leap:
        back = leap.pop()
        print(back, now_b)
    leap.append(now_b)

for num in leap:
    print(1, num)