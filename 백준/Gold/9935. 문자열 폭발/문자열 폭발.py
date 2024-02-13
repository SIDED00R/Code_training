import sys
input = sys.stdin.readline

line = input().rstrip('Wn')[:-1]
boom = input().rstrip('Wn')[:-1]
N = len(boom)
stack = []

for i in line:
    if not stack:
        if i == boom[0]:
            stack.append([i, 1])
        else:
            stack.append([i, 0])
    else:
        before_count = stack[-1][1]
        if i == boom[before_count]:
            stack.append([i, before_count + 1])
        elif i == boom[0]:
            stack.append([i, 1])
        else:
            stack.append([i, 0])
    if stack[-1][1] == N:
        for _ in range(N):
            stack.pop()
            
if stack == []:
    print("FRULA")
else:
    for case in stack:
        print(case[0], end = "")
        
