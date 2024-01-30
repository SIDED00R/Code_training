import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().rstrip('\n').split()))

num_count = [[0, 0]]
answer = 0

for num in A:
    now_max = 0
    for case in num_count:
        if num > case[0] and now_max < case[1]:
            now_max = case[1]
    num_count.append([num, now_max + num])     
    if answer < now_max + num:
        answer = now_max + num
        
print(answer)
    