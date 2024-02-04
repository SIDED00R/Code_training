import sys
input = sys.stdin.readline

N = int(input())

for i in range(N):
    first, second, third = map(int, input().rstrip('\n').split())
    if i == 0:
        max_dp = [first, second, third]
        min_dp = [first, second, third]
    else:
        
        max_dp = [max(max_dp[0], max_dp[1]) + first,  max(max_dp[0], max_dp[1], max_dp[2]) + second, max(max_dp[2], max_dp[1]) + third]
        min_dp = [min(min_dp[0], min_dp[1]) + first,  min(min_dp[0], min_dp[1], min_dp[2]) + second, min(min_dp[2], min_dp[1]) + third]
print(max(max_dp), min(min_dp))