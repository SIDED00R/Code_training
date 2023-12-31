def solution(alp, cop, problems):
    max_alp = alp
    max_cop = cop
    check_table = [[[[0, 1, 1], [1, 0, 1]] for _ in range(151)] for _ in range(151)]
    for i in range(alp, 151):
        for j in range(cop, 151):
            for problem in problems:
                alp_req, cop_req, alp_rwd, cop_rwd, cost = problem
                if i >= alp_req and j >= cop_req:
                    check_table[i][j].append([alp_rwd, cop_rwd, cost])
                if max_alp < alp_req:
                    max_alp = alp_req
                if max_cop < cop_req:
                    max_cop = cop_req
    
    time_table = [[0 for _ in range(max_cop + 1)] for _ in range(max_alp + 1)]
    for i in range(alp, max_alp  + 1):
        for j in range(cop, max_cop + 1):
            for case in check_table[i][j]:
                a, c, value = case
                if time_table[min(max_alp, i + a)][min(max_cop, j + c)] == 0 and (min(max_alp, i + a) != alp or min(max_cop, j + c) != cop):
                    time_table[min(max_alp, i + a)][min(max_cop, j + c)] = time_table[i][j] + value
                elif time_table[min(max_alp, i + a)][min(max_cop, j + c)] > time_table[i][j] + value:
                    time_table[min(max_alp, i + a)][min(max_cop, j + c)] = time_table[i][j] + value
                    
    for line in time_table:
        print(line)
    return time_table[max_alp][max_cop]