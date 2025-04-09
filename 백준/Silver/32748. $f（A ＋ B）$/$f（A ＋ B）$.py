def func(num):
    s_num = str(num)
    answer = ""
    for now_num in s_num:
        answer += str(line[int(now_num)])
    return int(answer)

def rev_func(num):
    s_num = str(num)
    answer = ""
    for now_num in s_num:
        answer += str(rev_line[int(now_num)])
    return int(answer)

line = list(map(int, input().split()))
rev_line = [0 for _ in range(10)]
for idx, val in enumerate(line):
    rev_line[val] = idx

a, b = map(int, input().split())

A = rev_func(a)
B = rev_func(b)
print(func(A + B))