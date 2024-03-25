import sys
input = sys.stdin.readline
from collections import defaultdict

def find(now, visited, relation, candy_nums):
    stack = [now]
    answer = []
    while stack:
        now = stack.pop()
        answer.append(now)
        if now in relation:
            able = relation[now]
            for case in able:
                if not visited[case]:
                    visited[case] = True
                    stack.append(case)
                    
    total_candy = 0                
    for idx in answer:
        total_candy += candy_nums[idx]
    return [len(answer), total_candy]

N, M, K = map(int, input().split())
candy_nums = [0] + list(map(int, input().split()))
relation = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    relation[a].append(b)
    relation[b].append(a)
    
visited = [False] * (N + 1)
group = [[]]
for idx in range(1, N + 1):
    if not visited[idx]:
        visited[idx] = True
        group.append(find(idx, visited, relation, candy_nums))
        
group_N = len(group)
dp = [[0 for _ in range(K)] for _ in range(group_N)]
for i in range(1, group_N):
    W, V = group[i]
    for j in range(1, K):
        if W <= j:
            dp[i][j] = max(dp[i - 1][j - W] + V, dp[i - 1][j])
        else:
            dp[i][j] = dp[i - 1][j]
            
print(dp[-1][-1])