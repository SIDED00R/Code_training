a, b = map(int, input().split())
answer = 1
for num in range(a, a - b, -1):
    answer *= num
for num in range(1, b + 1):
    answer /= num
print(int(answer))