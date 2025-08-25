while True:
    find = True
    try:
        line = list(map(int, input().split()))
        stack = [0 for _ in range(line[0] + 1)]
        for idx in range(1, line[0]):
            diff = abs(line[idx] - line[idx + 1])
            if diff >= line[0]:
                print('Not jolly')
                find = False
                break
            stack[diff] = 1
        if not find:
            continue
        if sum(stack) == line[0] - 1:
            print('Jolly')
        else:
            print('Not jolly')
    except:
        break