def able(n, x, y, structure, frame):

    if structure == 0:
        if y == 0 or (y > 0 and frame[x][y - 1] != "X" and frame[x][y - 1] <= 0) or (x > 0 and frame[x - 1][y] != "X" and frame[x - 1][y] >= 0) or (frame[x][y] != "X" and frame[x][y] >= 0):
            return True
    else:
        if y > 0 and ((frame[x][y - 1] != "X" and frame[x][y - 1] <= 0) or (x < n and frame[x + 1][y - 1] != "X" and frame[x + 1][y - 1] <= 0) or (x < n and x > 0 and frame[x + 1][y] != "X" and frame[x - 1][y] != "X" and frame[x + 1][y] >= 0 and frame[x - 1][y] >= 0)):
            return True
    return False

def solution(n, build_frame):
    # 없음: "X", 보: 1, 기둥: -1, 둘 다: 0
    frame = [["X" for _ in range(n + 1)] for _ in range(n + 1)]
    for item in build_frame:
        x, y, structure, case = item
        if structure == 0:
            if case == 0: #기둥 삭제
                if frame[x][y] == 0:
                    frame[x][y] = 1
                elif frame[x][y] == -1:
                    frame[x][y] = "X"
                else:
                    continue
                can = True
                for i in range(n + 1):
                    for j in range(n + 1):
                        if frame[i][j] == 0:
                            if able(n, i, j, 0, frame) and able(n, i, j, 1, frame):
                                continue
                            else:
                                can = False
                        elif frame[i][j] == -1:
                            if able(n, i, j, 0, frame):
                                continue
                            else:
                                can = False
                        elif frame[i][j] == 1:
                            if able(n, i, j, 1, frame):
                                continue
                            else:
                                can = False
                if can:
                    continue
                else:
                    if frame[x][y] == "X":
                        frame[x][y] = -1
                    else:
                        frame[x][y] = 0   
            else: # 기둥 설치
                if able(n, x, y, structure, frame):
                    if frame[x][y] == "X":
                        frame[x][y] = -1
                    else:
                        frame[x][y] = 0
        else:
            if case == 0: # 보 삭제
                if frame[x][y] == 0:
                    frame[x][y] = -1
                elif frame[x][y] == 1:
                    frame[x][y] = "X"
                else:
                    continue
                can = True
                for i in range(n + 1):
                    for j in range(n + 1):
                        if frame[i][j] == 0:
                            if able(n, i, j, 0, frame) and able(n, i, j, 1, frame):
                                continue
                            else:
                                can = False
                        elif frame[i][j] == -1:
                            if able(n, i, j, 0, frame):
                                continue
                            else:
                                can = False
                        elif frame[i][j] == 1:
                            if able(n, i, j, 1, frame):
                                continue
                            else:
                                can = False
                if can:
                    continue
                else:
                    if frame[x][y] == "X":
                        frame[x][y] = 1
                    else:
                        frame[x][y] = 0
            else: # 보 설치
                if able(n, x, y, structure, frame):
                    if frame[x][y] == "X":
                        frame[x][y] = 1
                    else:
                        frame[x][y] = 0
            
    answer = []
    for i in range(n + 1):
        for j in range(n + 1):
            if frame[i][j] != "X":
                if frame[i][j] == 0:
                    answer.append([i, j, 0])
                    answer.append([i, j, 1])
                elif frame[i][j] == 1:
                    answer.append([i, j, 1])
                elif frame[i][j] == -1:
                    answer.append([i, j, 0])
    answer = sorted(answer, key = lambda x:[x[0], x[1], x[2]])
    return answer