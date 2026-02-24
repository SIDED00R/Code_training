n = int(input())
stack = [0]

for _ in range(n):
    num = int(input())
    stack.append(num)
answer = 0
ans = -1
for i in range(1, n + 1):
    visited = [False for _ in range(n + 1)]
    visited[i] = True
    count = 1
    now = i
    while not visited[stack[now]]:
        visited[stack[now]] = True
        count += 1
        now = stack[now]
    if answer < count:
        answer = count
        ans = i

print(ans)