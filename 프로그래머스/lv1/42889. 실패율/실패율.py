def solution(N, stages):
    answer = [0 for _ in range(N)]
    stages = sorted(stages)
    for i in range(N):
        if stages[0] > N:
            break
        p = stages.count(stages[0]) / len(stages)
        answer[stages[0] - 1] = p
        if p == 1:
            break
        else:
            stages = stages[stages.count(stages[0]):]
    

    answer = sorted(enumerate(answer), key=lambda x : (-x[1],x[0]))
        
    return [i[0] + 1 for i in answer]