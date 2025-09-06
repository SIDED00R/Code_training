from fractions import Fraction

t = int(input())

def is_in_range(a, b, front, back):
    fu, fd = front
    bu, bd = back
    value = Fraction(a, b)
    low = Fraction(fu, fd)
    high = Fraction(bu, bd)
    return low <= value <= high

dic = {0: [[(0, 1), (1, 1)]]}
for idx in range(1, 11):
    stack = []
    before_stack = dic[idx - 1]
    mul = 3
    for now_case in before_stack:
        front, back = now_case
        fu, fd = front
        bu, bd = back
        stack.append([(fu * mul, fd * mul), (fu * mul + 1, fd * mul)])
        stack.append([(bu * mul - 1, bd * mul), (bu * mul, bd * mul)])
    dic[idx] = stack

for _ in range(t):
    a, b = map(int, input().split())
    for idx in range(11):
        find = False
        for now_case in dic[idx]:
            front, back = now_case
            if is_in_range(a, b, front, back):
                find = True
            if find:
                break
        if not find:
            break
    if not find:
        print(idx)
    else:
        print(-1)
            