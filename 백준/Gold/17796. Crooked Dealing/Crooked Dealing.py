from collections import defaultdict
import heapq

n, h = map(int, input().split())
max_people = n // h
line = list(map(int, input().split()))
dic = defaultdict(int)
for num in line:
    dic[num] += 1

heap = []
for number, count in dic.items():
    heapq.heappush(heap, [-count, number])

answer = []
for _ in range(max_people):
    if len(heap) < h:
        print("impossible")
        exit()
    keep = []
    now_ans = []
    for _ in range(h):
        count, number = heapq.heappop(heap)
        keep.append([count + 1, number])
        now_ans.append(number)
    for keep_case in keep:
        if keep_case[0] == 0:
            continue
        else:
            heapq.heappush(heap, keep_case)
    answer.append(now_ans)
for ans in answer:
    for num in ans:
        print(num, end = " ")
    print()
