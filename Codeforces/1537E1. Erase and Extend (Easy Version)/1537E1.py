import sys
input = sys.stdin.readline

n, k = map(int, input().split())
word = input().rstrip()
answer = word
for idx in range(1, n):
	front = word[:idx]
	back = word[idx:]
	if front < back:
		answer = front
		break
		
length = len(answer)
mul = k // length
answer *= mul + 1
print(answer[:k])