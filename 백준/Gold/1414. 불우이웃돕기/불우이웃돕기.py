import heapq

def find(num):
    if parent[num] == num:
        return num
    return find(parent[num])
        
def union(a, b):
    ap = find(a)
    bp = find(b)
    if ap == bp:
        return 0
    else:
        if ap > bp:
            parent[ap] = bp
        else:
            parent[bp] = ap
        return 1

n = int(input())
matrix = []
for _ in range(n):
    line = list(input())
    now_line = []
    for alp in line:
        if alp == '0':
            now_line.append(0)
            continue
        if alp.isupper():
            now = ord(alp) - 65 + 27
        else:
            now = ord(alp) - 97 + 1
        now_line.append(now)
    matrix.append(now_line)

total = 0
stack = []
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 0:
            continue
        else:
            total += matrix[i][j]
            heapq.heappush(stack, [matrix[i][j], i, j])

parent = [i for i in range(n)]
answer = 0
count = 0
while stack:
    weight, i, j = heapq.heappop(stack)
    if union(i, j) == 0:
        continue
    else:
        answer += weight
        count += 1

if count != n - 1:
    print(-1)
else:
    print(total - answer)