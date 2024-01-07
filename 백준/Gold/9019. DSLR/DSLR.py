import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    A, B = map(int, input().split())
    stack = [[A, ""]]
    new_stack = []
    answer = []
    find = False
    now_case = {}
    while stack:
        before, move = stack.pop()
        for i in range(4):
            if i == 0:
                now = (before * 2) % 10000
                if now not in now_case:
                    now_case[now] = 0
                    new_stack.append([now, move + "D"])
                if now == B:
                    print(move + "D")
                    find = True
                    break
            elif i == 1:
                now = (before + 9999) % 10000
                if now not in now_case:
                    now_case[now] = 0
                    new_stack.append([now, move + "S"])
                if now == B:
                    print(move + "S")
                    find = True
                    break
            elif i == 2:
                now = (before % 1000) * 10 + before // 1000
                if now not in now_case:
                    now_case[now] = 0
                    new_stack.append([now, move + "L"])
                if now == B:
                    print(move + "L")
                    find = True
                    break
            elif i == 3:
                now = before // 10 + 1000 * (before % 10)
                if now not in now_case:
                    now_case[now] = 0
                    new_stack.append([now, move + "R"])
                if now == B:
                    print(move + "R")
                    find = True
                    break
        if find:
            break
        if not stack:
            stack = new_stack[:]
            new_stack = []
    