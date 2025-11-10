import sys
input = sys.stdin.readline

n = int(input())
line = sorted(list(map(int, input().split())))

dp = [0, 0]
power_matrix = [pow(2, i, 1000000007) for i in range(1, n)]
for i in range(1, n):
    dp.append((dp[-1] * 2 + (power_matrix[i - 1] - 1) * (line[i] - line[i - 1])) % 1000000007)
print(sum(dp) % 1000000007)
