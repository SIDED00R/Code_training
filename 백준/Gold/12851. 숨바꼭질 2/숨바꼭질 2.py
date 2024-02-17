import sys
input = sys.stdin.readline

N, K = map(int, input().split())

locate = [0] * 100001
visited = [False] * 100001
locate[N] = 1
stack = [N]
count = 0

find = False
next_stack = []
while stack:
    now = stack.pop()
    if now == K:
        find = True
        break
    if now + 1 <= 100000 and not visited[now + 1]:
        if not locate[now + 1]:
            next_stack.append(now + 1)
        locate[now + 1] += locate[now]
    if now - 1 >= 0 and not visited[now - 1]:
        if  not locate[now - 1]:
            next_stack.append(now - 1)
        locate[now - 1] += locate[now]
    if now * 2 <= 100000 and not visited[now * 2]:
        if not locate[now * 2]:
            next_stack.append(now * 2)
        locate[now * 2] += locate[now]
    if not stack:
        count += 1
        stack = next_stack[:]
        for num in stack:
            visited[num] = True
        next_stack = []  
print(count)
print(locate[K])