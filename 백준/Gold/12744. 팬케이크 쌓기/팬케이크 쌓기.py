from collections import deque

n = int(input())

def change(i, case):
    case = [list(x) for x in case]
    front = case[:i + 1]
    back = case[i + 1:]
    front = front[::-1]
    for idx in range(len(front)):
        if front[idx][1] == "+":
            front[idx][1] = "-"
        else:
            front[idx][1] = "+"
    new_case = front + back
    return tuple(tuple(x) for x in new_case)

stack = []
for _ in range(n):
    idx, sim = input().split()
    idx = int(idx)
    stack.append((idx, sim))

dic = {}
dic[tuple(stack)] = 0
able_case = deque()
able_case.append([tuple(stack), 0])
goal = tuple((i, "+") for i in range(1, n + 1))
while able_case:
    now_case, w = able_case.popleft()
    if now_case == goal:
        print(w)
        break
    for i in range(n):
        next_case = change(i, now_case)
        if next_case in dic:
            continue
        else:
            dic[tuple(next_case)] = 0
            able_case.append([next_case, w + 1])

            