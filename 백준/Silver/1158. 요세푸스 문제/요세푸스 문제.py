n, k = map(int, input().split())
l = [i + 1 for i in range(n)]
answer = []
now_idx = -1
while l:
    now_idx = (now_idx + k) % len(l)
    answer.append(l[now_idx])
    l = l[:now_idx] + l[now_idx + 1:]
    now_idx -= 1
answer = list(map(str, answer))
print(f"<{', '.join(answer)}>")