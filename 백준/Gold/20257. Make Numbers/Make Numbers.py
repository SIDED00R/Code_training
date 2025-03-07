from itertools import permutations, product

def evaluate_expression(expr):
    try:
        return eval(expr)
    except:
        return None

def func(s):
    ans = set()
    ops = ['+', '-', '*']
    for now_set in s:
        n = len(now_set)
        if n < 2:
            continue
        for op_comb in product(ops, repeat=n-1):
            expr = str(now_set[0])
            for i in range(n-1):
                expr += op_comb[i] + str(now_set[i+1])
            value = evaluate_expression(expr)
            if value is not None and value >= 0:
                ans.add(int(value))
    return len(ans)

nums = input().split()
able_set = set()

for perm in permutations(nums):
    able_set.add(perm)

s = set()
for case in able_set:
    s.add(case)
    s.add((case[0] + case[1], case[2], case[3]))
    s.add((case[0], case[1] + case[2], case[3]))
    s.add((case[0], case[1], case[2] + case[3]))
    s.add((case[0] + case[1], case[2] + case[3]))
    s.add((case[0] + case[1] + case[2], case[3]))
    s.add((case[0], case[1] + case[2] + case[3]))

print(func(s))