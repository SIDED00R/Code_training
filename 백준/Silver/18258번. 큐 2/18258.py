from collections import deque
import sys
input = sys.stdin.readline 

n = int(input())
q = deque()
for _ in range(n):
	line = input().rstrip("\n")
	if line == "front":
		if q:
			print(q[0])
		else:
			print(-1)
	elif line == "back":
		if q:
			print(q[-1])
		else:
			print(-1)
	elif line == "pop":
		if q:
			out = q.popleft()
		else:
			out = -1
		print(out)
	elif line == "size":
		print(len(q))
	elif line == "empty":
		if q:
			print(0)
		else:
			print(1)
	else:
		_, num = line.split()
		num = int(num)
		q.append(num)