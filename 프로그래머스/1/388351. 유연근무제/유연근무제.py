def solution(schedules, timelogs, startday):
    schedules = list(map(str, schedules))
    answer = 0
    for idx in range(len(schedules)):
        h = int(schedules[idx][:-2])
        m = int(schedules[idx][-2:])
        count = 0
        people_time = list(map(str, timelogs[idx] * 2))
        for time in people_time[8 - startday:13 - startday]:
            th = int(time[:-2])
            tm = int(time[-2:])
            
            if h * 60 + m + 10 >= th * 60 + tm:
                count += 1

        if count == 5:
            answer += 1

    return answer