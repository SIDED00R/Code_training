def findroad(nodenum, answer, cango, dic, K):
    for key, value in dic[nodenum].items():
        if not cango[int(key)][0]:
            if cango[int(nodenum)][1] + value <= K:
                cango[int(key)][0] = True
                cango[int(key)][1] = cango[int(nodenum)][1] + value
                answer += 1
                answer = findroad(key, answer, cango, dic, K)
        else:
            if cango[int(nodenum)][1] + value <= cango[int(key)][1]:
                cango[int(key)][0], cango[int(key)][1] = True, cango[int(nodenum)][1] + value
                answer = findroad(key, answer, cango, dic, K)
            
    return answer

def solution(N, road, K):
    dic = {f"{num}" : {} for num in range(1, N + 1)}
    cango = [[False, K + 1], [True, 0]] + [[False, K + 1] for _ in range(1, N)]
    
    for node in road:
        first = str(node[0])
        second = str(node[1])
        time = node[2]
        
        if second in dic[first]:
            if dic[first][second] > time:
                dic[first][second] = time
                dic[second][first] = time 
        else:
            dic[first][second] = time
            dic[second][first] = time
    
    answer = 1
     
    return findroad("1", answer, cango, dic, K) 