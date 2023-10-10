import sys

N, M = map(int,input().split())

d = {}
answer = []

for i in range(N):
    name = input()
    d[name] = 0

for i in range(M):
    name = input()
    if name in d:
        answer.append(name)

print(len(answer))
answer = sorted(answer)
for people in answer:
    print(people)


