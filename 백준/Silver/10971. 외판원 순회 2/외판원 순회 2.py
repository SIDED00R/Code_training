from itertools import permutations

n = int(input())
cost_matrix = []
for _ in range(n):
    cost_matrix.append(list(map(int, input().split())))
    
answer = 1e9
for case in permutations(range(1, n), n - 1):
    before = 0
    find = True
    now_cost = 0
    for num in case:
        if cost_matrix[before][num] != 0:
            now_cost += cost_matrix[before][num]
            before = num
        else:
            find = False
            break
    if cost_matrix[before][0] != 0 and find:
        now_cost += cost_matrix[before][0]
        answer = min(answer, now_cost)
    
        
        
print(answer)