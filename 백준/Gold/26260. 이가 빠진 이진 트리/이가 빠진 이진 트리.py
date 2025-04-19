from collections import deque

n = int(input())
l = list(map(int, input().split()))
add = int(input())
for idx in range(n):
    if l[idx] == -1:
        l[idx] = add

l = sorted(l)
answer = []
stack = deque()
stack.append(l)
while stack:
    now_l = stack.popleft()
    length = len(now_l)
    if length == 1:
        answer.append(now_l[0])
    else:
        half = length // 2
        answer.append(now_l[half])
        stack.append(now_l[:half])
        stack.append(now_l[half + 1:])

def postorder(idx, n):
    if idx > n:
        return
    postorder(idx * 2, n)
    postorder(idx * 2 + 1, n)
    print(answer[idx - 1], end = " ")

postorder(1, n)