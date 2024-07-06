def check(i, j, sign):
    if sign == "d":
        next_i, next_j = i + 1, j
    elif sign == "r":
        next_i, next_j = i, j + 1
    elif sign == "u":
        next_i, next_j = i - 1, j
    elif sign == "l":
        next_i, next_j = i, j - 1
    if 0 <= next_i < n and 0 <= next_j < n and matrix[next_i][next_j] == 0:
        return True
    else:
        return False

n = int(input())
find = int(input())
matrix = [[0 for _ in range(n)] for _ in range(n)]
num = n ** 2
dic = {"d":[1, 0], "l":[0, -1], "r":[0, 1], "u":[-1, 0]}
change = {"d":"r", "l":"d", "r":"u", "u":"l"}
i, j = 0, 0
matrix[i][j] = num
sign = "d"
answer = [0, 0]
for idx in range(1, num):
    if check(i, j, sign):
        i, j = i + dic[sign][0], j + dic[sign][1]
    else:
        sign = change[sign]
        i, j = i + dic[sign][0], j + dic[sign][1]
    matrix[i][j] = num - idx
    if num - idx == find:
        answer = [i, j]
        
for l in matrix:
    for number in l:
        print(number, end = " ")
    print()
print(answer[0] + 1, answer[1] + 1)



