import sys

N, M = map(int, input().split())

d = {}
arr = []

for i in range(N):
    name = sys.stdin.readline().split()
    d[name[0]] = i + 1
    arr.append(name[0])


for i in range(M):
    quiz = sys.stdin.readline().split()
    quiz = quiz[0]
    if quiz.isnumeric():
        print(arr[int(quiz) - 1])
    else:
        print(d[quiz])

