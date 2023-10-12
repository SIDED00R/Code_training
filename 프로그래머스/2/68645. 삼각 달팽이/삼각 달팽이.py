def solution(n):
    answer = [[0 for i in range(n)] for j in range(n)]
    i, j = 0, 0
    answer[i][j] = 1
    down = True
    count = 2
    
    while count != n * (n + 1) // 2 + 1:
        
        if down: 
            if i + 1 == n or answer[i + 1][j] != 0:
                down = False
                side = True
                continue
            else:
                i += 1
                answer[i][j] = count
                count += 1
                
        elif side:
            if j + 1 == n or answer[i][j + 1] != 0:
                side = False
                up = True
                continue
            else:
                j += 1
                answer[i][j] = count
                count += 1
                
        elif up:
            if answer[i - 1][j - 1] != 0:
                up = False
                down = True
                continue
            else:
                i -= 1
                j -= 1
                answer[i][j] = count
                count += 1
            
    ans = []   
    for idx in range(len(answer)):
        ans += answer[idx][:idx+1]
    return ans