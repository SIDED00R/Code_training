import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip('\n').split())
know_num = list(map(int, input().rstrip('\n').split()))

partys = []
nodes = [[] for _ in range(N + 1)]
for i in range(M):
    line = list(map(int, input().rstrip('\n').split()))
    partys.append(line[1:])
    for num in line[1:]:
        nodes[num].append(i)
        
if know_num[0] == 0:
    print(M)
else:
    visited = [False] * (N + 1)
    true_party = [False] * M
    for num in know_num[1:]:
        if not visited[num]:
            stack = [num]
            while stack:
                now = stack.pop()
                for party_idx in nodes[now]:
                    if not true_party[party_idx]:
                        true_party[party_idx] = True
                        for people in partys[party_idx]:
                            if not visited[people]:
                                visited[people] = True
                                stack.append(people)                        
    print(M - sum(true_party))