import math

def solution(fees, records):
    dic = {}
    total_time = {}
    answer = []
    for record in records:
        time, num, state = record.split()
        if state == "IN":
            dic[num] = time
        else:
            in_hour, in_min = map(int, dic[num].split(":"))
            out_hour, out_min = map(int, time.split(":"))
            total = (out_hour - in_hour) * 60 + (out_min - in_min)
            if num in total_time:
                total_time[num] += total
            else:
                total_time[num] = total
            dic[num] = ""
    for key, value in dic.items():
        if value == "":
            continue
        else:
            in_hour, in_min = map(int, value.split(":"))
            out_hour, out_min = 23, 59
            total = (out_hour - in_hour) * 60 + (out_min - in_min)
            if key in total_time:
                total_time[key] += total
            else:
                total_time[key] = total
            
    for key, value in total_time.items():
        answer.append([key, value])
    answer = sorted(answer, key = lambda x: int(x[0]))
    answer = [i[1] for i in answer]
    
    ans = []
    for case in answer:
        if case <= fees[0]:
            ans.append(fees[1])
        else:
            add = math.ceil((case - fees[0]) / fees[2])
            ans.append(fees[1] + add * fees[3])

    return ans