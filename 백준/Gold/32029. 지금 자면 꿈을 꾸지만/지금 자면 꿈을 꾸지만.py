def check(l, spend_time, key_time):
    answer = 0
    now_time = spend_time
    for time in l:
        if time >= now_time + key_time:
            answer += 1
            now_time += key_time

    return answer, now_time
    
n, a, b = map(int, input().split())
line = list(map(int, input().split()))
line.sort()

answer, time = check(line, 0, a)

for ai in range(a):
    spend = ai * b
    if line[-1] < spend:
        break
    else:
        for idx in range(len(line)):
            now_answer, time = check(line[:idx], 0, a)
            time += spend
            if line[-1] < time:
                break
            else:
                after_answer, at = check(line[idx:], time, a - ai)
                now_answer += after_answer
                answer = max(now_answer, answer)

print(answer)

