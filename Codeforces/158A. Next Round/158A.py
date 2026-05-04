n, k = map(int, input().split())
sort_line = sorted(list(map(int, input().split())))
key = max(1, sort_line[-k])
answer = 0
for num in sort_line:
    if num >= key:
        answer += 1
print(answer)