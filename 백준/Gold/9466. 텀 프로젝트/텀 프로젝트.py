import sys
input = sys.stdin.readline

def counter(arr, num):
    next_idx = arr[num] - 1
    count = 1
    while next_idx != num:
        next_idx = arr[next_idx] - 1
        count += 1
    return count    

T = int(input())
for _ in range(T):
    answer = 0
    n = int(input())
    line = list(map(int, input().rstrip('\n').split()))
    group = [0] * n
    now_group_num = 0
    start_stack = []
    for idx, num in enumerate(line):
        next_idx = num - 1 
        if group[idx] == 0:
            now_group_num += 1
            group[idx] = now_group_num
            while group[next_idx] == 0:
                group[next_idx] = now_group_num
                next_idx = line[next_idx] - 1
            if group[next_idx] == now_group_num:
                start_stack.append(next_idx)
    for num in start_stack:
        answer += counter(line, num)
    print(n - answer)    
    
        
    