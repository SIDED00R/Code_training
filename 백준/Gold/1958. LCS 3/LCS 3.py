import sys
input = sys.stdin.readline

first_letter = list(input().rstrip('\n'))
second_letter = list(input().rstrip('\n'))
third_letter = list(input().rstrip('\n'))
N, M, L = len(first_letter), len(second_letter), len(third_letter)
dp = [[[0 for _ in range(L + 1)] for _ in range(M + 1)] for _ in range(N + 1)]
for i in range(N):
    for j in range(M):
        for k in range(L):
            if first_letter[i] == second_letter[j] == third_letter[k]:
                dp[i + 1][j + 1][k + 1] = dp[i][j][k] + 1
            else:
                dp[i + 1][j + 1][k + 1] = max(dp[i][j + 1][k + 1], dp[i + 1][j][k + 1], dp[i + 1][j + 1][k])
print(dp[-1][-1][-1])