import math
def solution(progresses, speeds):
    time = [math.ceil((100 - progresses[i])/speeds[i]) for i in range(len(progresses))]
    
    now = time[0]
    count = 1
    answer = []
    print(time)
    for i in time[1:]:
        if i > now:
            answer.append(count)
            count = 1
            now = i
        else:
            count += 1 
    return answer + [count]