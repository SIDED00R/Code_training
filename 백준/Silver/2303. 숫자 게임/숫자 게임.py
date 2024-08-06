from itertools import permutations

n = int(input())
answer = 0
total_end = 0
for idx in range(n):
    end = 0
    for case in permutations(list(map(int, input().split())), 3):
        end = max(sum(case) % 10, end)
    if total_end <= end:
        total_end = end
        answer = idx
        
print(answer + 1)