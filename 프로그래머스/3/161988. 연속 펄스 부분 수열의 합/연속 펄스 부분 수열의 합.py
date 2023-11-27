def solution(sequence):
    answer = 0
    case1, case2 = [], []
    for idx, num in enumerate(sequence):
        if idx % 2 == 0:
            case1.append(num)
            case2.append(-num)
        else:
            case1.append(-num)
            case2.append(num)
            
    for case in [case1, case2]:
        total = 0
        for n in case:
            total += n
            if total > answer:
                answer = total
            if total < 0:
                total = 0
        
    return answer