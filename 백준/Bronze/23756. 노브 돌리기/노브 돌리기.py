n = int(input())
start = int(input())
answer = 0
for _ in range(n):
    num = int(input())
    answer += min(abs(num - start), 360 - abs(num - start))
    start = num

print(answer)