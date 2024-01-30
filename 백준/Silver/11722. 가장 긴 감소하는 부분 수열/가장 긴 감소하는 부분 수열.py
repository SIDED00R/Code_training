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

stack = [0]
count_list = []
max_num = 0

for num in A[::-1]:
    if stack[-1] < num:
        stack.append(num)
        count_list.append([num, len(stack) - 1])
        max_num = len(stack) - 1
    else:
        idx = find_idx(stack, num)
        stack[idx] = num
        count_list.append([num, idx])

print(max_num)