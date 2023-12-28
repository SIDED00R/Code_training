def solution(rectangle, characterX, characterY, itemX, itemY):
    coordinate = [[0 for _ in range(152)] for _ in range(152)]
    for case in rectangle:
        left_x, left_y, right_x, right_y = case
        for x in range(left_x * 3, right_x * 3 + 1):
            for y in range(left_y * 3 , right_y * 3 + 1):
                coordinate[x][y] = 1
    match = False
    now_x, now_y = characterX * 3, characterY * 3
    d_x = [-1, -1, 0, 1, 1, 1, 0, -1]
    d_y = [0, 1, 1, 1, 0, -1, -1, -1]
    patterns = [[2, 4, 6, 0], [2, 4, 6, 0], [0, 2, 4, 6]]
    count = 0
    while not match:
        pattern = []
        for idx in range(8):
            pattern.append(coordinate[now_x + d_x[idx]][now_y + d_y[idx]])
        N = sum(pattern)
        if N == 5 or N == 6:
            for i in range(0, 8, 2):
                if pattern[i] == 0:
                    now_x += d_x[patterns[1][i // 2]]
                    now_y += d_y[patterns[1][i // 2]]
                    count += 1
        
        elif N == 3:
            for i in range(1, 8, 2):
                if pattern[i] == 1:
                    now_x += d_x[patterns[2][i // 2]]
                    now_y += d_y[patterns[2][i // 2]]
                    count += 1

        elif N == 7:
            for i in range(1, 8, 2):
                if pattern[i] == 0:
                    now_x += d_x[patterns[0][i // 2]]
                    now_y += d_y[patterns[0][i // 2]]
                    count += 1
                    
        if now_x == itemX * 3 and now_y == itemY * 3:
            answer = count
            count = 0
        if now_x == characterX * 3 and now_y == characterY * 3:
            if answer > count:
                answer = count
            match = True

    return answer // 3