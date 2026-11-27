from collections import deque

n, k = map(int, input().split())
line = tuple(map(int, input().split()))
q = deque([line])
dic = {}
dic[line] = 1

while q:
	now_line = q.popleft()
	now_weight = dic[now_line]
	for i in range(n - k + 1):
		front = now_line[:i]
		change = now_line[i:i + k][::-1]
		back = now_line[i + k:]
		change_line = front + change + back
		if change_line in dic:
			continue
		else:
			dic[change_line] = now_weight + 1
			q.append(change_line)
			
ans = tuple(range(1, n + 1))
if ans in dic:
	print(dic[ans] - 1)
else:
	print(-1)