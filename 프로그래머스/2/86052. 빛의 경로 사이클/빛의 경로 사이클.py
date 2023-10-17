def light(able, arr, i, j, k, count):
    col = len(able)
    row = len(able[0])
    while True:
        count += 1
        if i < 0:
            i = col + i
        if j < 0:
            j = row + j
        if able[i][j][k] == 1:
            return count - 1
        able[i][j][k] = 1
        if k == 0:
            case = arr[i - 1][j]
            if case == "S":
                i, j, k = i - 1, j, 0
            elif case == "R":
                i, j, k = i - 1, j, 3
            elif case == "L":
                i, j, k = i - 1, j, 2
            
        elif k == 1:
            case = arr[(i + 1)%col][j]
            if case == "S":
                i, j, k =(i + 1)%col, j, 1
            elif case == "R":
                i, j, k = (i + 1)%col, j, 2
            elif case == "L":
                i, j, k = (i + 1)%col, j, 3
    
        elif k == 2:
            case = arr[i][j - 1]
            if case == "S":
                i, j, k = i, j - 1, 2
            elif case == "R":
                i, j, k = i, j - 1, 0
            elif case == "L":
                i, j, k = i, j - 1, 1
            
        elif k == 3:
            case = arr[i][(j + 1)%row]
            if case == "S":
                i, j, k = i, (j + 1)%row, 3
            elif case == "R":
                i, j, k = i, (j + 1)%row, 1
            elif case == "L":
                i, j, k = i, (j + 1)%row, 0

def solution(grid):
    answer = []
    
    # 각 칸을 리스트로 만들기
    arr = [list(i) for i in grid]
    
    # 가능한 케이스 다 적기
    able = []
    col = len(arr)
    row = len(arr[0])
    for i in range(col):
        line = []
        for j in range(row):
            line.append([0, 0, 0, 0]) # 상하좌우로 해당 위치로 빛을 보냈는지
        able.append(line)
        
    for i in range(len(able)):
        for j in range(len(able[i])):
            for k in range(len(able[i][j])):
                if able[i][j][k] == 0:
                    count = 0
                    count = light(able, arr, i, j, k, count)
                    answer.append(count)   
    
    answer.sort()
    return answer
