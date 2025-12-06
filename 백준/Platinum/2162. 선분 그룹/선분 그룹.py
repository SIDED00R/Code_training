from collections import defaultdict

def ccw(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])

def intersect(A, B, C, D):
    ccw1 = ccw(A, B, C)
    ccw2 = ccw(A, B, D)
    ccw3 = ccw(C, D, A)
    ccw4 = ccw(C, D, B)

    if ccw1 * ccw2 < 0 and ccw3 * ccw4 < 0:
        return True

    if ccw1 == 0 and min(A[0], B[0]) <= C[0] <= max(A[0], B[0]) and min(A[1], B[1]) <= C[1] <= max(A[1], B[1]):
        return True
    if ccw2 == 0 and min(A[0], B[0]) <= D[0] <= max(A[0], B[0]) and min(A[1], B[1]) <= D[1] <= max(A[1], B[1]):
        return True
    if ccw3 == 0 and min(C[0], D[0]) <= A[0] <= max(C[0], D[0]) and min(C[1], D[1]) <= A[1] <= max(C[1], D[1]):
        return True
    if ccw4 == 0 and min(C[0], D[0]) <= B[0] <= max(C[0], D[0]) and min(C[1], D[1]) <= B[1] <= max(C[1], D[1]):
        return True

    return False

n = int(input())

lines = []
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    lines.append([x1, y1, x2, y2])

dic = defaultdict(list)
for i in range(n):
    for j in range(i + 1, n):
        A = lines[i][:2]
        B = lines[i][2:]
        C = lines[j][:2]
        D = lines[j][2:]
        if intersect(A, B, C, D):
            dic[i].append(j)
            dic[j].append(i)

visited = [0 for _ in range(n)]
count = 0
for now in range(n):
    if visited[now] == 0:
        count += 1
        visited[now] = count
        stack = [now]
        while stack:
            out = stack.pop()
            for next_node in dic[out]:
                if visited[next_node] == 0:
                    visited[next_node] = count
                    stack.append(next_node)

answer_dic = defaultdict(int)
for num in visited:
    answer_dic[num] += 1

print(len(answer_dic))
print(max(answer_dic.values()))