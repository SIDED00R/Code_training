from bisect import bisect_right

n = int(input())
bridge = []
for _ in range(n):
    a, b = map(int, input().split())
    bridge.append([a, b])

bridge.sort()

weight = []
num_list = []

weight.append(0)
num_list.append(bridge[0][1])

for now_case in bridge[1:]:
    _, num = now_case
    if num_list[-1] < num:
        weight.append(len(num_list))
        num_list.append(num)
    else:
        idx = bisect_right(num_list, num)
        num_list[idx] = num
        weight.append(idx)

answer = []
find = max(weight)
for answer_idx in range(n - 1, -1, -1):
    if weight[answer_idx] == find:
        find -= 1
    else:
        answer.append(answer_idx)

print(len(answer))
for num in answer[::-1]:
    print(bridge[num][0])
    