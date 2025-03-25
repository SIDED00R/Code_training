import copy

def solution(mats, park):
    answer = -1
    mats = sorted(mats)

    col = len(park[0])
    row = len(park)
    count = 1
    before_matrix = copy.deepcopy(park)

    for i in range(row):
        for j in range(col):
            if park[i][j] == "-1":
                answer = 1

    if answer == -1:
        return -1
    answer = -1

    while True:
        matrix = [[0 for _ in range(col)] for _ in range(row)]
        find = False
        for i in range(row - count):
            for j in range(col - count):
                if before_matrix[i][j] == "-1" and before_matrix[i + 1][j] == "-1" and before_matrix[i][j + 1] == "-1" and before_matrix[i + 1][j + 1] == "-1":
                    matrix[i][j] = "-1"
                    find = True
        if find:
            count += 1
            before_matrix = copy.deepcopy(matrix)
        else:
            break

    for mat in mats:
        if count < mat:
            break
        else:
            answer = mat

    return answer