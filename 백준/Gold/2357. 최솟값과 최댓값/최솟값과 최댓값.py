import sys, math
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def make_tree(start_idx, end_idx, node_idx):
    if start_idx == end_idx:
        tree[node_idx] = (num_list[start_idx], num_list[end_idx])
        return
    mid_idx = (start_idx + end_idx) // 2
    make_tree(start_idx, mid_idx, node_idx * 2)
    make_tree(mid_idx + 1, end_idx, node_idx * 2 + 1)
    left = tree[node_idx * 2]
    right = tree[node_idx * 2 + 1]
    tree[node_idx] = (min(left[0], right[0]), max(left[1], right[1]))

def find(start_idx, end_idx, node_idx, a, b):
    if b < start_idx or end_idx < a:
        return (1e20, -1e20)
    if a <= start_idx and end_idx <= b:
        return tree[node_idx]
    mid_idx = (start_idx + end_idx) // 2
    front = find(start_idx, mid_idx, node_idx * 2, a, b)
    back = find(mid_idx + 1, end_idx, node_idx * 2 + 1, a, b)
    return (min(front[0], back[0]), max(front[1], back[1]))
n, m = map(int, input().split())
num_list = []
for _ in range(n):
    num_list.append(int(input()))

h = math.floor(math.log2(n)) + 1
tree = [(0, 0) for _ in range(2 ** (h + 1))]

make_tree(0, n - 1, 1)

for _ in range(m):
    a, b = map(int, input().split())
    answer = find(0, n - 1, 1, a - 1, b - 1)
    print(answer[0], answer[1])