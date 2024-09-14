n = int(input())
max_count = 0
answer = []
for num in range(n + 1):
    now_answer = [n, num]
    while now_answer[-1] >= 0:
        now_answer.append(now_answer[-2] - now_answer[-1])
    now_answer.pop()
    if len(now_answer) > max_count:
        answer = now_answer[:]
        max_count = len(now_answer)
print(max_count)
for num in answer:
    print(num, end = " ")