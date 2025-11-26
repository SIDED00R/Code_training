d, n, u, t = map(int, input().split())

route = {}
for _ in range(n):
    s, e = map(int, input().split())
    route[(s, e)] = 1

first_time = [[0, 1] for _ in range(2 ** d)]
stack = [1]
while stack:
    out = stack.pop()
    before_total, height = first_time[out]
    if out * 2 >= 2 ** d:
        continue
    if (out, out * 2) not in route and (out, out * 2 + 1) not in route:
        stack.append(out * 2)
        first_time[out * 2] = [before_total + u + t * height, height + 1]
        stack.append(out * 2 + 1)
        first_time[out * 2 + 1] = [before_total + u + t * height, height + 1]
    elif (out, out * 2) not in route:
        stack.append(out * 2)
        first_time[out * 2] = [before_total + u + t * (height - 1), height]
    elif (out, out * 2 + 1) not in route:
        stack.append(out * 2 + 1)
        first_time[out * 2 + 1] = [before_total + u + t * (height - 1), height]

first_answer = sorted(first_time)[-1][0]

count = 0
for now in first_time:
    if now != [0, 1]:
        count += 1

deep = 0
idx = 1
while True:
    deep += 1
    if idx * 2 < 2 ** d:
        if first_time[idx * 2 + 1] == [0, 1] and first_time[idx * 2] == [0, 1]:
            break
        elif first_time[idx * 2 + 1] == [0, 1]:
            idx = idx * 2
        else:
            idx = idx * 2 + 1
    else:
        break

second_answer = count * u * 2 - (deep - 1) * u

if first_answer == second_answer:
    print(":blob_twintail_thinking:")
elif first_answer < second_answer:
    print(":blob_twintail_aww:")
else:
    print(":blob_twintail_sad:")