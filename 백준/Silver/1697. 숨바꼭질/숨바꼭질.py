import sys
input = sys.stdin.readline

N, K = map(int, input().split())

board = [False] * 100001
stack = [N]
next_stack = []
count = 1
while stack:
    now = stack.pop()
    if now == K:
        print(count - 1)
        break
    if now + 1 <= 100000 and not board[now + 1]:
        next_stack.append(now + 1)
        board[now + 1] = True
    if now - 1 >= 0 and not board[now - 1]:
        next_stack.append(now - 1)
        board[now - 1] = True
    if now * 2 <= 100000 and not board[now * 2]:
        next_stack.append(now * 2)
        board[now * 2] = True
        
    if not stack:
        count += 1
        stack = next_stack[:]
        next_stack = []