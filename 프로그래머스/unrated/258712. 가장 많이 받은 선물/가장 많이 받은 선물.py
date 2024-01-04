def solution(friends, gifts):
    N = len(friends)
    dic = {}
    for idx, friend in enumerate(friends):
        dic[friend] = idx
    table = [[0 for _ in range(N)] for _ in range(N)]
    give = [0] * N
    get = [0] * N
    for gift in gifts:
        A, B = gift.split()
        a_idx = dic[A]
        b_idx = dic[B]
        table[a_idx][b_idx] += 1
        give[a_idx] += 1
        get[b_idx] += 1
        
    next_gift = [0] * N
    for i in range(N):
        for j in range(N):
            if table[i][j] > table[j][i]:
                next_gift[i] += 1
            elif table[i][j] < table[j][i]:
                next_gift[j] += 1
            else:
                if give[i] - get[i] > give[j] - get[j]:
                    next_gift[i] += 1
                elif give[i] - get[i] < give[j] - get[j]:
                    next_gift[j] += 1

    return max(next_gift) // 2