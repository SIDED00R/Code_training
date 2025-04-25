from itertools import product

n, k = map(int, input().split())
line = list(input().split())

ans_list = []
for i in range(1, len(str(n)) + 1):
    for l in product(line, repeat = i):
        ans_list.append(int("".join(l)))

ans_list.sort()
while ans_list[-1] > n:
    ans_list.pop()
print(ans_list[-1])
            