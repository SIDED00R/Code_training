import sys
input = sys.stdin.readline

N, M = map(int, input().split())
total_tree_tall = list(map(int, input().split()))
max_tall = max(total_tree_tall)
min_tall = 0

while min_tall <= max_tall:
    now = (max_tall + min_tall) // 2
    get_total = 0
    for tree in total_tree_tall:
        if tree > now:
            get_total += tree - now
    if get_total >= M:
        min_tall = now + 1
    else:
        max_tall = now - 1
print(max_tall)