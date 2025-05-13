def func(l, d):
    for num in l:
        d[num] += 1
    return d

n, m = map(int, input().split())
line = list(map(int, input().split()))
front = line[:n]
back = line[n:]

front_dic = {i:0 for i in range(1, m + 1)}
back_dic = {i:0 for i in range(1, m + 1)}

front_dic = func(front, front_dic)
back_dic = func(back, back_dic)

answer = 0
for k, v in front_dic.items():
    answer += v * (n - back_dic[k])

print(answer)