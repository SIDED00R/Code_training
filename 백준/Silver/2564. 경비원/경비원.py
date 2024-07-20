row, col = map(int, input().split())
n = int(input())

store = []
for _ in range(n + 1):
    i, j = map(int, input().split())
    if i == 1:
        store.append([col, j, i])
    elif i == 2:
        store.append([0, j, i])
    elif i == 3:
        store.append([col - j, 0, i])
    else:
        store.append([col - j, row, i])
   
        
def root(s_i, s_j, now_i, now_j, now_length, cycle, col, row, side):
    if side == 1:
        if now_i == s_i and 0 <= s_j < now_j:
            now_length += now_j - s_j
            return min(now_length, cycle - now_length)
        else:
            now_length += now_j
            now_j = 0
            answer = root(s_i, s_j, now_i, now_j, now_length, cycle, col, row, 3)
            
    elif side == 2:
        if now_i == s_i and now_j < s_j <= row:
            now_length += s_j - now_j
            return min(now_length, cycle - now_length)
        else:
            now_length += row - now_j
            now_j = row
            answer = root(s_i, s_j, now_i, now_j, now_length, cycle, col, row, 4)
            
    elif side == 3:
        if now_j == s_j and 0 <= s_i < now_i:
            now_length += now_i - s_i
            return min(now_length, cycle - now_length)
        else:
            now_length += now_i
            now_i = 0
            answer = root(s_i, s_j, now_i, now_j, now_length, cycle, col, row, 2)
            
    elif side == 4:
        if now_j == s_j and now_i < s_i <= col:
            now_length += s_i - now_i
            return min(now_length, cycle - now_length)
        else:
            now_length += col - now_i
            now_i = col
            answer = root(s_i, s_j, now_i, now_j, now_length, cycle, col, row, 1)
    return answer
    
cycle = (row + col) * 2
s_i, s_j, s_side = store[-1]
answer = 0
for case in store[:-1]:
    now_i, now_j, now_side = case
    answer += root(s_i, s_j, now_i, now_j, 0, cycle, col, row, now_side)
    
print(answer)
    