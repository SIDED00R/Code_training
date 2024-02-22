import sys
input = sys.stdin.readline

TC = int(input())
for _ in range(TC):
    N, M, W = map(int, input().rstrip('\n').split())
    cases = []
    for _ in range(M):
        S, E, T = map(int, input().rstrip('\n').split())
        cases.append([S, E, T])
        cases.append([E, S, T])
    for _ in range(W):
        S, E, T = map(int, input().rstrip('\n').split())
        cases.append([S, E, -T])
    weights = [0] * (N + 1)
    weights[cases[0][1]] = 0
    for count in range(N):
        if count == N - 1:
            save_weights = weights[:]
        for case in cases:
            s, e, t = case
            weights[e] = min(weights[e], weights[s] + t)
    if save_weights == weights:
        print("NO")
    else:
        print("YES")
    
    