def solution(n, t, m, timetable):
    timetable = sorted(timetable, reverse = True)
    for idx, time in enumerate(timetable):
        hour, minute = map(int,time.split(":"))
        timetable[idx] = hour * 60 + minute
        
    now = 9 * 60
    for i in range(n):
        
        able = True
        count = 0
        while timetable and count < m and able:
            if timetable[-1] <= now:
                count += 1
                people = timetable.pop()
            else:
                able = False
        now += t
    a_h, a_m = "", ""
    if count == m:
        people -= 1
        a_h = str(people // 60)
        a_m = str(people % 60)
        
    else:
        answer = 9 * 60 + t * (n - 1)
        a_h = str(answer // 60)
        a_m = str(answer % 60)
        
    return f"{a_h.zfill(2)}:{a_m.zfill(2)}"