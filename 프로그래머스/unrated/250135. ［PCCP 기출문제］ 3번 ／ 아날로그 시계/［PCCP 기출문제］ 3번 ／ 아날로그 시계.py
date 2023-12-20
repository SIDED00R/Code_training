def solution(h1, m1, s1, h2, m2, s2):
    num = 60 * 60 * 12
    hour = [0] * num
    minute = [0] * num
    second = [0] * num
    check = [0] * num
    now_hour = 0
    now_minute = 0
    now_second = 0
    for i in range(num):
        hour[i] = round(now_hour,4)
        minute[i] = round(now_minute,2)
        second[i] = now_second
        now_hour += 1/120
        now_minute += 0.1
        now_second += 6
        if round(now_minute,2) % 360 == 0:
            now_minute = 0
        if now_second % 360 == 0:
            now_second = 0    
    check[0] = 1
    for j in range(1, num):
        if second[j] != 0:
            if hour[j] < second[j] and hour[j - 1] > second[j - 1]:
                check[j] += 1
            if minute[j] < second[j] and minute[j - 1] > second[j - 1] or minute[j] == second[j]:
                check[j] += 1
        else:
            if hour[j] < 360 and hour[j - 1] > second[j - 1]:
                check[j] += 1
            if minute[j] < 360 and minute[j - 1] > second[j - 1] or minute[j] == second[j]:
                check[j] += 1
    answer = 0
    if h1 >= 12:
        h1 -= 12
        h2 -= 12
    elif h2 >= 12:
        h2 -= 12
        answer += sum(check)
    
    start_time = h1 * 3600 + m1 * 60 + s1
    finish_time = h2 * 3600 + m2 * 60 + s2
    
    if start_time == 0:
        return answer + sum(check[:finish_time + 1])
    else:
        return answer + sum(check[:finish_time + 1]) - sum(check[:start_time + 1])