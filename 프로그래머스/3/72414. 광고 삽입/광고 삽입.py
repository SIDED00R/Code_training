def solution(play_time, adv_time, logs):
    p_h, p_m, p_s = map(int, play_time.split(":"))
    time = [0] * (p_h * 60 * 60 + p_m * 60 + p_s + 1)
    for log in logs:
        start, end = log.split("-")
        s_h, s_m, s_s = map(int, start.split(":"))
        start_time = s_h * 60 * 60 + s_m * 60 + s_s
        e_h, e_m, e_s = map(int, end.split(":"))
        end_time = e_h * 60 * 60 + e_m * 60 + e_s
        time[start_time] += 1
        time[end_time] -= 1
    for idx in range(1, len(time)):
        time[idx] += time[idx - 1]
        
    a_h, a_m, a_s = map(int, adv_time.split(":"))
    check_time = a_h * 60 * 60 + a_m * 60 + a_s
    
    max_time = sum(time[:check_time])
    for i in range(len(time) - check_time):
        if i == 0:
            now_time = max_time
            answer = 0
        else:
            now_time -= time[i - 1]
            now_time += time[check_time + i - 1]
            if max_time < now_time:
                max_time = now_time
                answer = i
    answer_h = answer // 3600
    answer %= 3600
    answer_m = answer // 60
    answer %= 60
    answer_s = answer
    return f"{answer_h:02d}:{answer_m:02d}:{answer_s:02d}"