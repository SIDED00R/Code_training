n = int(input())
line = list(map(int, input().split()))
max_num = max(line)
min_num = min(line)
max_idx = []
min_idx = []
for idx in range(len(line)):
    if line[idx] == min_num:
        min_idx.append(idx)
    if line[idx] == max_num:
        max_idx.append(idx)
now_min_idx = min_idx.pop()
now_max_idx = max_idx.pop()
answer = abs(now_min_idx - now_max_idx)
while True:
    try:
        if now_min_idx > now_max_idx:
            now_min_idx = min_idx.pop()
        elif now_min_idx < now_max_idx:
            now_max_idx = max_idx.pop()
        else:
            answer = 0
            break
        answer = min(answer, abs(now_min_idx - now_max_idx))
    except:
        break
print(answer + 1)



