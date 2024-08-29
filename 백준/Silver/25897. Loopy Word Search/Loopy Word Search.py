t = int(input())
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
dic = {0:"R", 1:"L", 2:"D", 3:"U"}
for idx in range(t):
    matrix = []
    answer = []
    r, c = map(int, input().split())
    for _ in range(r):
        matrix.append(list(input()))
        
    s = int(input())
    for _ in range(s):
        letter = list(input())
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == letter[0]:
                    for k in range(4):
                        find = True
                        for letter_idx in range(len(letter)):
                            ni = (i + di[k] * letter_idx) % r
                            nj = (j + dj[k] * letter_idx) % c
                            if matrix[ni][nj] != letter[letter_idx]:
                                find = False
                                break
                        if find:
                            answer.append([k, i, j, letter])

    print(f"Word search puzzle #{idx + 1}:")
    for cases in answer:
        print(dic[cases[0]], cases[1] + 1, cases[2] + 1, "".join(cases[3]))
    print()
        