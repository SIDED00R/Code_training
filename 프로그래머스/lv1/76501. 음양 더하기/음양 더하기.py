def solution(absolutes, signs):
    answer = 0
    for idx, x in enumerate(signs):
        if x:
            answer += absolutes[idx]
        else:
            answer -= absolutes[idx]
        
    return answer