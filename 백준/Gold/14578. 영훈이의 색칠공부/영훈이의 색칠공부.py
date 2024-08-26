def fact(n):
    answer = 1
    for num in range(1, n + 1):
        answer *= num
        answer %= 1000000007
    return answer

n = int(input())

if n == 1:
    print(0)

elif n == 2:
    print(2)

else:
    dp = [0] * (n + 1)
    dp[2] = 1
    for num in range(3, n + 1):
        dp[num] = (num - 1) * (dp[num - 2] + dp[num - 1]) % 1000000007
        
    print(dp[-1] * fact(n) % 1000000007)