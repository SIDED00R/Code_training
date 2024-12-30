import math

def sum_tree(start, end, idx):
    if start == end:
        total_list[idx] = num_list[start - 1]
        return total_list[idx]
    mid = (start + end) // 2
    total_list[idx] = sum_tree(start, mid, idx * 2) + sum_tree(mid + 1, end, idx * 2 + 1)
    return total_list[idx]

def update_tree(start, end, idx, target, diff):
    if target < start or target > end:
        return
    total_list[idx] += diff
    if start != end:
        mid = (start + end) // 2
        update_tree(start, mid, idx * 2, target, diff)
        update_tree(mid + 1, end, idx * 2 + 1, target, diff)

def query_tree(start, end, idx, left, right):
    if left > end or right < start: 
        return 0
    if left <= start and end <= right: 
        return total_list[idx]
    mid = (start + end) // 2
    return query_tree(start, mid, idx * 2, left, right) + query_tree(mid + 1, end, idx * 2 + 1, left, right)

n, m, k = map(int, input().split())

total_list = [0] * (2 ** (math.ceil(math.log2(n)) + 1))
num_list = []

for _ in range(n):
    num = int(input())
    num_list.append(num)

sum_tree(1, n, 1)

for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        before = num_list[b - 1]
        num_list[b - 1] = c
        diff = c - before
        update_tree(1, n, 1, b, diff)
    elif a == 2:
        print(query_tree(1, n, 1, b, c))
