import itertools

N = int(input())
case = ['9', '8', '7', '6', '5', '4', '3', '2', '1', '0']
total_case = []
answer = []
for i in range(1, 11):
    total_case += list(itertools.combinations(case, i))
for abc in total_case:
    arr = ''.join(abc)
    answer.append(arr)
answer = list(map(int, answer))
answer = sorted(answer)
if N >= len(answer):
    print(-1)
else:
    print(answer[N])

