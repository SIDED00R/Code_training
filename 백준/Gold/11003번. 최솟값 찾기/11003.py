from collections import deque
import sys
input = sys.stdin.readline

n, l = map(int, input().split())
line = list(map(int, input().split()))

dq = deque()
answer = []

for i in range(n):
	while dq and line[dq[-1]] >= line[i]:
		dq.pop()
	dq.append(i)
	if dq[0] <= i - l:
		dq.popleft()
	answer.append(line[dq[0]])

sys.stdout.write(" ".join(map(str, answer)))