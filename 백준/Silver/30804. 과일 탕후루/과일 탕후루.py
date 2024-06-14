import sys
input = sys.stdin.readline
n = int(input())
tang_huru = list(input().rstrip('\n').split())

dic = {}
count = 0
answer = 0
total = 0
out_idx = 0
for idx in range(len(tang_huru)):
    fruit = tang_huru[idx]
    if fruit not in dic or dic[fruit] == 0:
        count += 1
        dic[fruit] = 1
    else:
        dic[fruit] += 1
    total += 1
    while count > 2:
        out_fruit = tang_huru[out_idx]
        out_idx += 1
        dic[out_fruit] -= 1
        total -= 1
        if dic[out_fruit] == 0:
            count -= 1
            
    if total > answer:
        answer = total
        
print(answer)
