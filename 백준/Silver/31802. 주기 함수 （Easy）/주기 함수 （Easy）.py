p = int(input())
line = list(map(int, input().split()))
a, b = map(int, input().split())

a_q, a_r = divmod(a, p)
b_q, b_r = divmod(b, p)

total = sum(line)

if a_q == b_q:
    answer = sum(line[a_r:b_r])
else:
    part1 = sum(line[a_r:]) 
    part2 = sum(line[:b_r]) 
    middle_part = total * (b_q - a_q - 1)
    answer = part1 + part2 + middle_part

print(answer)