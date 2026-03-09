def check(front, floor, sides):
    if front[0] != floor:
        return False
    for idx in range(3):
        if front[1:] == sides[idx:idx + 3]:
            return True
    return False

k = int(input())
for _ in range(k):
    line = list(map(int, input().split()))
    front = line[4:]
    find = False
    for idx in range(4):
        floor = line[idx]
        if idx == 0:
            sides = line[1:4] * 2
        elif idx == 1:
            sides = [line[2], line[0], line[3]] * 2
        elif idx == 2:
            sides = [line[0], line[1], line[3]] * 2
        elif idx == 3:
            sides = [line[0], line[2], line[1]] * 2
        if check(front, floor, sides):
            find = True
            break
    if find:
        print(1)
    else:
        print(0)