n = int(input())
answer = 0
for num in range(1, n // 3 + 1):
    a = num
    b = n - num * 2
    while a <= b:
        if b < num + a:
            answer += 1
        b -= 1
        a += 1

print(answer)