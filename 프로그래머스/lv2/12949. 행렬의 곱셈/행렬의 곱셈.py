def solution(arr1, arr2):
    row1 = range(len(arr1))
    col1 = range(len(arr1[0]))
    col2 = range(len(arr2[0]))
    answer = [[0 for _ in col2] for _ in row1]
    for i in row1:
        for j in col1:
            for k in col2:
                answer[i][k] += arr1[i][j] * arr2[j][k]
            
    return answer