def solution(maps):
    count = 1

    stack = [[0, 0, 1]]
    while len(stack) != 0:
        row, col, count = stack.pop(0)
        count += 1
        if row + 1 < len(maps) and (maps[row + 1][col] == 1 or maps[row + 1][col] > count):
            maps[row + 1][col] = count
            stack.append([row + 1, col, count])

        if col + 1 < len(maps[0]) and (maps[row][col + 1] == 1 or maps[row][col + 1] > count):
            maps[row][col + 1] = count
            stack.append([row, col + 1, count])
        
        if row > 0 and (maps[row - 1][col] == 1 or maps[row - 1][col] > count):
            maps[row - 1][col] = count
            stack.append([row - 1, col, count])
        
        if col > 0 and (maps[row][col - 1] == 1 or maps[row][col - 1] > count):
            maps[row][col - 1] = count
            stack.append([row, col - 1, count])
    if maps[-1][-1] == 1:
        return -1
    else:
        return maps[-1][-1]