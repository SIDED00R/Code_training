import sys
input = sys.stdin.readline

N, M = map(int, input().split())
move = {}

for _ in range(N + M):
    before, after = map(int, input().split())
    move[before] = after

board = [101] * 101
stack = [1]
count = 1
new_stack = []
find = False
while stack:
    now = stack.pop()
    for i in range(1, 7):
        if board[now + i] == 101:
            if now + i in move:
                new_stack.append(move[now + i])
                board[move[now + i]] = count
            else:
                new_stack.append(now + i)
                board[now + i] = count
            if board[-1] != 101:
                print(board[-1])
                find = True
                break
    if find:
        break
    else:
        if not stack:
            stack = new_stack[:]
            count += 1
            new_stack = []
