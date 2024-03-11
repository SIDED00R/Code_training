import sys
input = sys.stdin.readline

def find_parent(num, parent):
    if parent[num] != num:
        parent[num] = find_parent(parent[num], parent)
    return parent[num]

def union(first, second, parent):
    num1 = find_parent(first, parent)
    num2 = find_parent(second, parent)
    if num1 < num2:
        parent[num2] = num1
    else:
        parent[num1] = num2

N, M = map(int, input().rstrip('\n').split())
parent = [i for i in range(N)]
answer = 0
find = False
for i in range(M):
    first, second = map(int, input().rstrip('\n').split())
    if not find and find_parent(first, parent) == find_parent(second, parent):
        find = True
        answer = i + 1
    union(first, second, parent)
    
print(answer)