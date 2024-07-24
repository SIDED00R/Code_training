t = int(input())
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
for _ in range(t):
    answer = 0
    h, w = map(int, input().split())
    matrix = []
    for _ in range(h):
        matrix.append(list(input())) 
    key = list(input())
    if key[0] == "0":
        key = []
    
    stack = []
    stack_door = []
    for i in range(h):
        if matrix[i][0] == ".":
            stack.append([i, 0])
            matrix[i][0] = "*"
        elif matrix[i][0] == "$":
            stack.append([i, 0])
            answer += 1
            matrix[i][0] = "*" 
        elif matrix[i][0].isalpha():
            if 65 <= ord(matrix[i][0]) <= 90:
                stack_door.append([matrix[i][0], i, 0])
            else:
                key.append(matrix[i][0])
                stack.append([i, 0])
                matrix[i][0] = "*"
                
        if matrix[i][w - 1] == ".":
            stack.append([i, w - 1])
            matrix[i][w - 1] = "*"
        elif matrix[i][w - 1] == "$":
            stack.append([i, w - 1])
            answer += 1
            matrix[i][w - 1] = "*" 
        elif matrix[i][w - 1].isalpha():
            if 65 <= ord(matrix[i][w - 1]) <= 90:
                stack_door.append([matrix[i][w - 1], i, w - 1])
            else:
                key.append(matrix[i][w - 1])
                stack.append([i, w - 1])
                matrix[i][w - 1] = "*"
        
    for j in range(1, w - 1):
        if matrix[0][j] == ".":
            stack.append([0, j])
            matrix[0][j] = "*"
        elif matrix[0][j] == "$":
            stack.append([0, j])
            answer += 1
            matrix[0][j] = "*" 
        elif matrix[0][j].isalpha():
            if 65 <= ord(matrix[0][j]) <= 90:
                stack_door.append([matrix[0][j], 0, j])
            else:
                key.append(matrix[0][j])
                stack.append([0, j])
                matrix[0][j] = "*"
                
        if matrix[h - 1][j] == ".":
            stack.append([h - 1, j])
            matrix[h - 1][j] = "*"
        elif matrix[h - 1][j] == "$":
            stack.append([h - 1, j])
            answer += 1
            matrix[h - 1][j] = "*" 
        elif matrix[h - 1][j].isalpha():
            if 65 <= ord(matrix[h - 1][j]) <= 90:
                stack_door.append([matrix[h - 1][j], h - 1, j])
            else:
                key.append(matrix[h - 1][j])
                stack.append([h - 1, j])
                matrix[h - 1][j] = "*"
    
    next_door = []
    for case in stack_door:
        alp, i, j = case
        if chr(ord(alp) + 32) in key:
            stack.append([i, j])
            matrix[i][j] = "*"
        else:
            next_door.append([alp, i, j])
    stack_door = next_door[:]            
    while stack:
        now_i, now_j = stack.pop()
        for idx in range(4):
            next_i = now_i + di[idx]
            next_j = now_j + dj[idx]
            if 0 <= next_i < h and 0 <= next_j < w:
               if matrix[next_i][next_j] == ".":
                    stack.append([next_i, next_j])
                    matrix[next_i][next_j] = "*"
               elif matrix[next_i][next_j] == "$":
                    stack.append([next_i, next_j])
                    answer += 1
                    matrix[next_i][next_j] = "*" 
               elif matrix[next_i][next_j].isalpha():
                    if 65 <= ord(matrix[next_i][next_j]) <= 90:
                        stack_door.append([matrix[next_i][next_j], next_i, next_j])
                    else:
                        key.append(matrix[next_i][next_j])
                        stack.append([next_i, next_j])
                        matrix[next_i][next_j] = "*"
                        
        if not stack:
            next_door = []
            for case in stack_door:
                alp, i, j = case
                if chr(ord(alp) + 32) in key:
                    stack.append([i, j])
                    matrix[i][j] = "*"
                else:
                    next_door.append([alp, i, j])
            stack_door = next_door[:]
            
    print(answer)
