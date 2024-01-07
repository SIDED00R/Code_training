import sys
input = sys.stdin.readline

N, M = map(int, input().split())

paper = []
for _ in range(N):
    line = list(map(int, input().split()))
    paper.append(line)

case1 = [[[0, 0, 0, 0], [0, 1, 2 ,3]], [[0, 1, 2, 3], [0, 0, 0, 0]]]
case2 = [[[0, 0, 1, 1], [0, 1, 0, 1]]]
case3 = [[[0, 1, 2, 2], [0, 0, 0, 1]], [[0, 0, 0, 1], [0, 1, 2, 0]], [[0, 0, 1, 2], [0, 1, 1, 1]], [[0, 1, 1, 1], [2, 0, 1, 2]], [[0, 1, 2, 2], [1, 1, 0, 1]], [[0, 1, 1, 1], [0, 0, 1, 2]], [[0, 0, 1, 2], [0, 1, 0, 0]], [[0, 0, 0, 1], [0, 1, 2, 2]]]
case4 = [[[0, 1, 1, 2], [0, 0, 1, 1]], [[0, 0, 1, 1], [1, 2, 0, 1]], [[0, 1, 1, 2], [1, 0, 1, 0]], [[0, 0, 1, 1], [0, 1, 1, 2]]]
case5 = [[[0, 0, 0, 1], [0, 1, 2, 1]], [[0, 1, 1, 2], [1, 0, 1, 1]], [[0, 1, 1, 1], [1, 0, 1, 2]], [[0, 1, 1, 2], [0, 0, 1, 0]]]
total_case = [case1, case2, case3, case4, case5]
max_answer = 0
for i in range(N):
    for j in range(M):
        for case in total_case:
            for subcase in case:
                di = subcase[0]
                dj = subcase[1]
                now_total = 0
                try:
                    for idx in range(4):
                        now_total += paper[i + di[idx]][j + dj[idx]]
                    if now_total > max_answer:
                        max_answer = now_total
                except:
                    continue
                
print(max_answer)