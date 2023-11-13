def solution(genres, plays):
    dic1 = {}
    dic2 = {}
    answer = []
    for i in range(len(genres)):
        if genres[i] not in dic1:
            dic1[genres[i]] = plays[i]
        else:
            dic1[genres[i]] += plays[i]
        
        if genres[i] not in dic2:
            dic2[genres[i]] = [[plays[i], i]]
        else:
            dic2[genres[i]] += [[plays[i], i]]
    
    long_time = []
    for key, value in dic1.items():
        long_time.append([key, value])
    long_time = sorted(long_time, key = lambda x:x[1])
    
    while long_time:
        case = long_time.pop()
        genre = case[0]
        time = dic2[genre]
        if len(time) == 1:
            answer.append(time[0][1])
        else:
            time = sorted(time, key = lambda x:[x[0], -x[1]])
            for i in range(2):
                num = time.pop()
                answer.append(num[1])
        
    
    return answer