n = int(input())
answer = 1
for _ in range(n):
    answer *= 3
    answer %= 1000000007
print((answer - 1) % 1000000007)