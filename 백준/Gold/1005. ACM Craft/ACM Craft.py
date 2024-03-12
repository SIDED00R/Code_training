import sys
input = sys.stdin.readline
from collections import defaultdict, deque

T = int(input())
for _ in range(T):
    dic = defaultdict(list)
    N, K = map(int, input().rstrip('\n').split())
    total_weight = [0 for _ in range(N)]
    weight = list(map(int, input().rstrip('\n').split()))
    for _ in range(K):
        X, Y = map(int, input().rstrip('\n').split())
        dic[Y].append(X)
    goal = int(input())
    total_weight[goal - 1] = weight[goal - 1]
    stack = deque([goal])
    while stack:
        now = stack.popleft()
        for case in dic[now]:
            if total_weight[case - 1] < total_weight[now - 1] + weight[case - 1]:
                total_weight[case - 1] = total_weight[now - 1] + weight[case - 1]
                stack.append(case)
    print(max(total_weight))