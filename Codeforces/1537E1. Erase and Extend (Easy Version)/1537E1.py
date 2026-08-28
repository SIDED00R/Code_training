import sys
input = sys.stdin.readline
 
n, k = map(int, input().split())
word = input().rstrip()
length = len(word)
mul = k // length
answer = word * (mul + 1)
answer = answer[:k]
for idx in range(1, n):
	front = word[:idx]
	length = len(front)
	mul = k // length
	front *= mul + 1
	answer = min(answer, front[:k])
print(answer)