N = int(input())
M = int(input())
computer = [[] for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    computer[a - 1].append(b - 1)
    computer[b - 1].append(a - 1)

s = set([0])
stack = computer[0][:]
computer[0][:] = []
while stack != []:
    case = stack.pop()
    stack += computer[case][:]
    computer[case][:] = []
    s.add(case)

print(len(s) - 1)

