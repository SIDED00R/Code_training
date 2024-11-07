t = int(input())
d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
for _ in range(t):
    line = input()
    stack = ""
    for idx in range(len(line)):
        if line[idx] == " ":
            r = int(stack)
            break
        else:
            stack += line[idx]
    stack = ""
    for next_idx in range(idx + 1, len(line)):
        if line[next_idx] == " ":
            c = int(stack)
            break
        else:
            stack += line[next_idx]
    matrix = [[0 for _ in range(c)] for _ in range(r)]
    v_matrix = [[0 for _ in range(c)] for _ in range(r)]
    message = line[next_idx + 1:]
    c_message = ""
    for letter in message:
        if letter == " ":
            c_message += "0" * 5
        else:
            c_message += bin(ord(letter) - 64)[2:].zfill(5)

    i, j = 0, 0
    direction = 0
    v_matrix[i][j] = 1
    if c_message:
        matrix[i][j] = c_message[0]
    for letter in c_message[1:]:
        ni = i + d[direction][0]
        nj = j + d[direction][1]
        if 0 <= ni < r and 0 <= nj < c and not v_matrix[ni][nj]:
            v_matrix[ni][nj] = 1
            matrix[ni][nj] = letter
        else:
            direction = (direction + 1) % 4
            ni = i + d[direction][0]
            nj = j + d[direction][1]
            v_matrix[ni][nj] = 1
            matrix[ni][nj] = letter
        i = ni
        j = nj

    for l in matrix:
        for num in l:
            print(num, end = "")
    print()