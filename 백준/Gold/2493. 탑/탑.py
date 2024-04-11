import sys
input = sys.stdin.readline

N = int(input())
line = list(map(int, input().split()))

stack = []
answer = []
for idx, tower in enumerate(line):
    while stack:
        if stack[-1][0] < tower:
            stack.pop()
        else:
            answer.append(stack[-1][1])
            stack.append([tower, idx + 1])
            break
            
    if stack == []:
        answer.append(0)
        stack.append([tower, idx + 1])
            

for ans in answer:
    print(ans, end = " ")
