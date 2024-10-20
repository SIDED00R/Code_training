x, y = map(int, input().split())
total_case = []
for n in range(1, 64):
    for m in range(1, 64):
        one = "1" * n
        zero = "0" * m
        now = one + zero
        next_case = one
        while int(now, 2) <= y:
            if x <= int(now, 2):
                total_case.append(now)
            now += next_case
            if next_case == one:
                next_case = zero
            else:
                next_case = one

for n in range(1, 64):
    if x <= int(n * "1", 2) <= y:
        total_case.append(n * "1")

print(len(total_case))