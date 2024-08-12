n, a, b = map(int, input().split())
line = list(map(int, input().split()))
move_weight = {1 : {1 : 0, 2 : 1, 3 : 2, 4 : 1, 5 : 2, 6 : 3, 7 : 2, 8 : 3, 9 : 4, 10 : 3, 11 : 4, 12 : 5},
               2 : {1 : 1, 2 : 0, 3 : 1, 4 : 2, 5 : 1, 6 : 2, 7 : 3, 8 : 2, 9 : 3, 10 : 4, 11 : 3, 12 : 4},
               3 : {1 : 2, 2 : 1, 3 : 0, 4 : 3, 5 : 2, 6 : 1, 7 : 4, 8 : 3, 9 : 2, 10 : 5, 11 : 4, 12 : 3},
               4 : {1 : 1, 2 : 2, 3 : 3, 4 : 0, 5 : 1, 6 : 2, 7 : 1, 8 : 2, 9 : 3, 10 : 2, 11 : 3, 12 : 4},
               5 : {1 : 2, 2 : 1, 3 : 2, 4 : 1, 5 : 0, 6 : 1, 7 : 2, 8 : 1, 9 : 2, 10 : 3, 11 : 2, 12 : 3},
               6 : {1 : 3, 2 : 2, 3 : 1, 4 : 2, 5 : 1, 6 : 0, 7 : 3, 8 : 2, 9 : 1, 10 : 4, 11 : 3, 12 : 2},
               7 : {1 : 2, 2 : 3, 3 : 4, 4 : 1, 5 : 2, 6 : 3, 7 : 0, 8 : 1, 9 : 2, 10 : 1, 11 : 2, 12 : 3},
               8 : {1 : 3, 2 : 2, 3 : 3, 4 : 2, 5 : 1, 6 : 2, 7 : 1, 8 : 0, 9 : 1, 10 : 2, 11 : 1, 12 : 2},
               9 : {1 : 4, 2 : 3, 3 : 2, 4 : 3, 5 : 2, 6 : 1, 7 : 2, 8 : 1, 9 : 0, 10 : 3, 11 : 2, 12 : 1},
               10 : {1 : 3, 2 : 4, 3 : 5, 4 : 2, 5 : 3, 6 : 4, 7 : 1, 8 : 2, 9 : 3, 10 : 0, 11 : 1, 12 : 2},
               11 : {1 : 4, 2 : 3, 3 : 4, 4 : 3, 5 : 2, 6 : 3, 7 : 2, 8 : 1, 9 : 2, 10 : 1, 11 : 0, 12 : 1},
               12 : {1 : 5, 2 : 4, 3 : 3, 4 : 4, 5 : 3, 6 : 2, 7 : 3, 8 : 2, 9 : 1, 10 : 2, 11 : 1, 12 : 0},
               }

dp = [{} for _ in range(n + 1)]
dp[0][(1, 3)] = 0
for i in range(1, n + 1):
    for key, value in dp[i - 1].items():
        left, right = key
        next_number = line[i - 1]
        left_move = value + move_weight[left][next_number] + a
        right_move = value + move_weight[right][next_number] + b
        if (next_number, right) in dp[i]:
            dp[i][(next_number, right)] = min(dp[i][(next_number, right)], left_move)
        else:
            dp[i][(next_number, right)] = left_move
        if (left, next_number) in dp[i]:
            dp[i][(left, next_number)] = min(dp[i][(left, next_number)], right_move)
        else:
            dp[i][(left, next_number)] = right_move
            
answer = 1e10
for key, value in dp[-1].items():
    answer = min(value, answer)
        
print(answer)