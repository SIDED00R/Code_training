def solution(k, score):
    answer = []
    result = []
    for num in score:
        answer.append(num)
        for idx in range(len(answer)):
            if answer[idx] < answer[-1]:
                answer[-1], answer[idx] = answer[idx], answer[-1]
        answer = answer[:k]
        result.append(answer[-1])
        
    return result