n = int(input())
leaf_list = list(map(int, input().split()))
for idx in range(n - 1):
    if leaf_list[idx] < leaf_list[idx + 1]:
        print(-1)
        exit()

out = leaf_list.pop()
if out == 2:
    answer = [[1, 2]]
    top = [1, 2]
elif out == 1:
    answer = []
    top = [1]
else:
    print(-1)
    exit()

while leaf_list:
    out_num = leaf_list.pop()
    if out_num == 1:
        print(-1)
        exit()
    last_num = top[-1]
    left = out_num - len(top)
    for num in top:
        answer.append([num, last_num + 1])
        last_num += 1

    for idx in range(left):
        answer.append([num, last_num + 1])
        last_num += 1

    top = [top[-1] + i + 1 for i in range(out_num)]

print(len(answer) + 1)
for ans in answer:
    print(ans[0], ans[1])
