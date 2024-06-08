from collections import deque

dic = {chr(i):i - 96 for i in range(97, 97 + 8)}
di = [2, 1, -1, -2, -2, -1, 1, 2]
dj = [1, 2, 2, 1, -1, -2, -2, -1]
try:
    while True:
        check_box = [[False for _ in range(9)] for _ in range(9)]
        first, second = input().split()
        start_i, start_j = [dic[first[0]], int(first[1])]
        stack = deque()
        stack.append([start_i, start_j, 0])
        end_i, end_j = [dic[second[0]], int(second[1])]

        while stack:
            start_i, start_j, count = stack.popleft()
            if start_i == end_i and start_j == end_j:
                print(f"To get from {first} to {second} takes {count} knight moves.")
                break
            for idx in range(8):
                next_i = start_i + di[idx]
                next_j = start_j + dj[idx]
                if 1 <= next_i <= 8 and 1 <= next_j <= 8 and not check_box[next_i][next_j]:
                    check_box[next_i][next_j] = True
                    stack.append([next_i, next_j, count + 1])
        
except:
    pass    
    
  