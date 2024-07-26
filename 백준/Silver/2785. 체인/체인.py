import sys
n = int(input())
line = list(map(int, sys.stdin.readline().split()))
sorted_line = sorted(line)

find = False
i = 0
total_chain = 0
while not find:
    find = True
    total_chain += sorted_line[i]
    i += 1
    if n - i - 1 == total_chain:
        print(total_chain)
    elif n - 1 - i < total_chain:
        print(n - i)
    else:
        find = False
     