from collections import defaultdict
a, b, c = map(int, input().split())
dic = defaultdict(int)
for i in range(1, a + 1):
    for j in range(1, b + 1):
        for k in range(1, c + 1):
            dic[i + j + k] += 1
    
answer = -1
max_num = -1
for k, v in dic.items():
    if max_num < v:
        answer = k
        max_num = v
    elif max_num == v:
        answer = min(answer, k)
print(answer)