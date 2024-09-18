n, m = map(int, input().split())
j = int(input())
start = 1
end = m
answer = 0
for _ in range(j):
    now = int(input())
    if start <= now <= end:
        continue
    elif now > end:
        answer += (now - end)
        start += (now - end)
        end = now
    elif start > now:
        answer += (start - now)
        end -= (start - now)
        start = now

print(answer)