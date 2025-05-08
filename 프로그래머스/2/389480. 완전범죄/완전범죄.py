def solution(info, n, m):
    answer = 1e9
    dp = [[-1 for _ in range(m)] for _ in range(n)]
    si, sj = info[0]
    stack = set()
    if sj < m:
        dp[0][sj] = 0
        stack.add((0, sj))
    if si < n:
        dp[si][0] = 0    
        stack.add((si, 0))
    next_stack = stack
    for idx in range(1, len(info)):
        di, dj = info[idx]
        next_stack = set()
        for now_case in stack:
            i, j = now_case
            ni = i + di
            nj = j + dj
            if nj < m and dp[i][nj] != idx:
                dp[i][nj] = idx
                next_stack.add((i, nj))
            if ni < n and dp[ni][j] != idx:
                dp[ni][j] = idx
                next_stack.add((ni, j))
        if next_stack:
            stack = next_stack
        else:
            answer = -1
            break
            
    if answer == -1:            
        return answer
    else:
        for ans in next_stack:
            if ans[0] < answer:
                answer = ans[0]
        return answer