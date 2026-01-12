from itertools import permutations

n = int(input())
line = list(map(int, input().split()))
for now in sorted(permutations(line, n)):
    able = [-1] * (2 * n)
    find = True
    for now_num in now:
        if not find:
            break
        for idx in range(2 * n):
            if able[idx] == -1:
                able[idx] = now_num
                if idx + now_num + 1 < 2 * n and able[idx + now_num + 1] == -1:
                    able[idx + now_num + 1] = now_num
                    break
                else:
                    find = False
                    break
    if find:
        print(*able)
        exit()
print(-1)
                