from lib2to3.pgen2.pgen import DFAState
import sys
input = sys.stdin.readline

first_letter = list(input().rstrip('\n'))
second_letter = list(input().rstrip('\n'))
N, M = len(first_letter), len(second_letter)
dp = [[0 for _ in range(N)] for _ in range(M)]
for i in range(M):
    for j in range(N):
        if i == 0:
            if second_letter[i] == first_letter[j]:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i][j - 1]    
        else:
            if j == 0:
                if second_letter[i] == first_letter[j]:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j]        
            else:
                if second_letter[i] == first_letter[j]:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - 1] + 1)
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])  
                
print(dp[-1][-1])