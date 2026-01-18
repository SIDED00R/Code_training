from collections import defaultdict

m = int(input())
line = input()
total_answer = 1e10
for n in range(1, m + 1):
    dic = defaultdict(lambda: defaultdict(int))
    for i in range((len(line) - 1) // n + 1):
        for j in range(n):
            try:
                now = line[i * n + j]
                dic[j][now] += 1
            except:
                break
    answer = 0
    for _, now_case in dic.items():
        total = 0
        max_value = 0
        for k, v in now_case.items():
            total += v
            max_value = max(max_value, v)
        answer += total - max_value
    total_answer = min(total_answer, answer)
print(total_answer)