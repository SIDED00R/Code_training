def solution(commands):
    answer = []
    table = [[[0, False, False, False, False] for _ in range(51)] for _ in range(51)]
    for line in commands:
        command = line.split()
        
        if command[0] == "UPDATE":
            if len(command) == 4:
                r = int(command[1])
                c = int(command[2])
                now_r, now_c = r, c
                before = table[r][c]
                while before[1]:
                    now_r = before[1]
                    now_c = before[2]
                    before = table[now_r][now_c]
                table[now_r][now_c][0] = command[3]
            else:
                for i in range(51):
                    for j in range(51):
                        if table[i][j][0] == command[1]:
                            table[i][j][0] = command[2]  
                            
        elif command[0] == "MERGE":
            r1, c1, r2, c2 = map(int, command[1:])
            
            front_before = table[r1][c1]
            front_before_r, front_before_c = r1, c1
            while front_before[1]:
                front_before_r, front_before_c = front_before[1], front_before[2]
                front_before = table[front_before_r][front_before_c]
                
            back_before = table[r2][c2]
            back_before_r, back_before_c = r2, c2
            while back_before[1]:
                back_before_r, back_before_c = back_before[1], back_before[2]
                back_before = table[back_before_r][back_before_c]
            
            if front_before_r == back_before_r and front_before_c == back_before_c:
                continue
            
            front_after = table[r1][c1]
            front_after_r, front_after_c = r1, c1
            while front_after[3]:
                front_after_r, front_after_c = front_after[3], front_after[4]
                front_after = table[front_after_r][front_after_c]
                
            back_after = table[r2][c2]
            back_after_r, back_after_c = r2, c2
            while back_after[3]:
                back_after_r, back_after_c = back_after[3], back_after[4]
                back_after = table[back_after_r][back_after_c]
            
            if front_before[0] != 0:
                back_before[0] = 0
                back_before[1] = front_after_r
                back_before[2] = front_after_c
                front_after[3], front_after[4] = back_before_r, back_before_c
            else:
                back_after[3] = front_before_r
                back_after[4] = front_before_c
                front_before[1], front_before[2] = back_after_r, back_after_c
                
        elif command[0] == "UNMERGE":
            r = int(command[1])
            c = int(command[2])
            value = 0
            before = table[r][c]
            now_r, now_c = r, c
            while before[1]:
                now_r, now_c = before[1], before[2]
                before = table[now_r][now_c]
            if before[0] != 0:
                value = before[0]
                before[0] = 0
            
            now = table[now_r][now_c]
            while now[3]:
                next_r, next_c = now[3], now[4]
                table[now_r][now_c] = [0, False, False, False, False]
                now = table[next_r][next_c]
                now_r, now_c = next_r, next_c
            table[now_r][now_c] = [0, False, False, False, False]
            table[r][c][0] = value
            
        elif command[0] == "PRINT":
            r = int(command[1])
            c = int(command[2])
            before = table[r][c]
            while before[1]:
                now_r, now_c = before[1], before[2]
                before = table[now_r][now_c]
            if before[0] == 0:
                answer.append("EMPTY")
            else:
                answer.append(before[0])

    return answer