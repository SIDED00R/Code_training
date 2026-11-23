from collections import deque

n, k = map(int, input().split())
dp = [-1 for _ in range(200000)]
q = deque()

dp[n] = n
q.append(n)
while dp[k] == -1:
	out = q.popleft()
	if 0 <= out - 1 and dp[out - 1] == -1:
		dp[out - 1] = out
		q.append(out - 1)
	if 200000 > out + 1 and dp[out + 1] == -1:
		dp[out + 1] = out
		q.append(out + 1)
	if 200000 > out * 2 and dp[out * 2] == -1:
		dp[out * 2] = out
		q.append(out * 2)
		
answer = [k]
now = k
while now != n:
	now = dp[now]
	answer.append(now)
	
print(len(answer) - 1)
print(" ".join(map(str, answer[::-1])))