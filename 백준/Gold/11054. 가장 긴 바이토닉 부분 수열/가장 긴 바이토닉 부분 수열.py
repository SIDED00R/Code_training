import sys
input = sys.stdin.readline

def find_idx(stack, num):
    start = 0
    end = len(stack) - 1
    while True:
        mid = (start + end) // 2
        if stack[mid] < num:
            start = mid
        else:
            end = mid
        if start + 1 >= end:
            return end

N = int(input())
A = list(map(int, input().rstrip('\n').split()))

stack_lower = [0]
stack_upper = [0]
count_lower_list = []
count_upper_list = []
max_num = 0

for num in A:
    if stack_lower[-1] < num:
        stack_lower.append(num)
        count_lower_list.append([num, len(stack_lower) - 1])
    else:
        idx = find_idx(stack_lower, num)
        stack_lower[idx] = num
        count_lower_list.append([num, idx])
  
for num in A[::-1]:
    if stack_upper[-1] < num:
        stack_upper.append(num)
        count_upper_list.append([num, len(stack_upper) - 1])
    else:
        idx = find_idx(stack_upper, num)
        stack_upper[idx] = num
        count_upper_list.append([num, idx])

for i in range(N):
    now_count = count_lower_list[i][1] + count_upper_list[N - i - 1][1]
    if max_num < now_count:
        max_num = now_count
        
print(max_num - 1)