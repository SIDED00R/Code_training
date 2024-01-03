import copy

def check(metrix, target, case, change):
    for i in range(len(metrix[0])):
        if metrix[0][i] != target[0][i]:
            change.append([0, i, 1])
            case += 1
    for j in range(len(metrix)):
        if metrix[j][0] != target[j][0]:
            change.append([j, 0, 0])
            case += 1
    return case

def solution(beginning, target):
    if beginning[0][0] == target[0][0]:
        case1 = 0
        change1 = []
        metrix = copy.deepcopy(beginning)
        case1 = check(metrix, target, case1, change1)     
        case2 = 2
        change2 = [[0, 0, 0], [0, 0, 1]]
        metrix = copy.deepcopy(beginning)
        for i in range(len(metrix)):
            for j in range(len(metrix[0])):
                if i * j == 0:
                    metrix[i][j] = 1 - metrix[i][j]
        metrix[0][0] = target[0][0]       
        case2 = check(metrix, target, case2, change2)
    else:
        case1 = 1
        change1 = [[0, 0, 0]]
        metrix = copy.deepcopy(beginning)
        for i in range(len(metrix)):
            for j in range(len(metrix[0])):
                if i == 0:
                    metrix[i][j] = 1 - metrix[i][j]
        case1 = check(metrix, target, case1, change1)     
        case2 = 1
        change2 = [[0, 0, 1]]
        metrix = copy.deepcopy(beginning)
        for i in range(len(metrix)):
            for j in range(len(metrix[0])):
                if j == 0:
                    metrix[i][j] = 1 - metrix[i][j]     
        case2 = check(metrix, target, case2, change2)
    if case1 > case2 :
        change = change2
    else:
        change = change1
        
    check_matrix = [[0 for _ in range(len(beginning[0]))] for _ in range(len(beginning))]
    for turn in change:
        i, j, go = turn
        if go == 0:
            for check_matrix_i in range(len(check_matrix)):
                for check_matrix_j in range(len(check_matrix[0])):
                    if i == check_matrix_i:
                        check_matrix[check_matrix_i][check_matrix_j] += 1
        else:
            for check_matrix_i in range(len(check_matrix)):
                for check_matrix_j in range(len(check_matrix[0])):
                    if j == check_matrix_j:
                        check_matrix[check_matrix_i][check_matrix_j] += 1    
    for i in range(len(target)):
        for j in range(len(target[0])):
            if abs(beginning[i][j] - (check_matrix[i][j] % 2)) != target[i][j]:
                return -1
    return len(change)