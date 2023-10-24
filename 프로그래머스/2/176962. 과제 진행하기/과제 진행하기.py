def solution(plans):
    answer = []
    plans = sorted(plans, key = lambda x: x[1])
    keep = []
    for plan in plans:
        subject, now, time = plan
        now_h, now_m = map(int, now.split(":"))
        if keep == []:
            keep.append([subject, now_h, now_m, int(time)])
        else:
            total_time = (now_h - keep[-1][1]) * 60 + now_m - keep[-1][2]
            while True:
                if keep == []:
                    break
                s, h, m, t = keep.pop()
                if total_time >= t:
                    answer.append(s)
                    total_time -= t
                else:
                    keep.append([s, h, m, t - total_time])
                    break

            keep.append([subject, now_h, now_m, int(time)])               
        
    while keep != []:
        s, h, m, t = keep.pop()
        answer.append(s)
    return answer