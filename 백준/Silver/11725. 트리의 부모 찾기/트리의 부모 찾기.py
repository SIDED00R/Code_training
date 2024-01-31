import sys
input = sys.stdin.readline

N = int(input())
nodes = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    front, back = map(int, input().rstrip('\n').split())
    nodes[front].append(back)
    nodes[back].append(front)
    
answer = [0] * (N + 1)
stack = [1]
while stack:
    now = stack.pop()
    for next_idx in nodes[now]:
        if answer[next_idx] == 0 and next_idx > 1:
            stack.append(next_idx)
            answer[next_idx] = now
            
for ans in answer[2:]:
    print(ans)