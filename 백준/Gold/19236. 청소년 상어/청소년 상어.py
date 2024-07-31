import copy

di = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dic = {}
matrix = [[[] for _ in range(4)] for _ in range(4)]
for i in range(4):
    line = list(map(int, input().split()))
    for j in range(len(line)):
        matrix[i][j // 2].append(line[j])
        if j % 2 == 0:
            dic[line[j]] = [i, j // 2]
        
num, d = matrix[0][0]
del dic[matrix[0][0][0]]
matrix[0][0] = [-1, d]
dic[-1] = [0, 0]
answer = num
now = num

def shark(matrix, dic):
    global answer, now
    
    for num in range(1, 17):
        if num in dic:
            i, j = dic[num]
            num, d = matrix[i][j]
            for case in range(8):
                next_i, next_j = i + di[(d + case - 1) % 8 + 1], j + dj[(d + case - 1) % 8 + 1]
                if 0 <= next_i < 4 and 0 <= next_j < 4 and 0 <= matrix[next_i][next_j][0] <= 16:
                    number, direct = matrix[next_i][next_j]
                    dic[number] = [i, j]
                    dic[num] = [next_i, next_j]
                    matrix[i][j] = [number, direct]
                    matrix[next_i][next_j] = [num, (d + case - 1) % 8 + 1]
                    break
    i, j = dic[-1]
    num, d = matrix[i][j]
    
    keep_matrix = copy.deepcopy(matrix)
    keep_dic = copy.deepcopy(dic)
    for mul in range(1, 4):
        next_i, next_j = i + di[d] * mul, j + dj[d] * mul
        if 0 <= next_i < 4 and 0 <= next_j < 4 and 1<= matrix[next_i][next_j][0] <= 16: 
            number, direct = matrix[next_i][next_j]
            del dic[number]
            dic[-1] = [next_i, next_j]
            matrix[i][j] = [0, 0]
            matrix[next_i][next_j] = [-1, direct]
            now += number
            answer = max(answer, now)
            shark(matrix, dic)
            matrix = copy.deepcopy(keep_matrix)
            dic = copy.deepcopy(keep_dic)
            now -= number
  
            
shark(matrix, dic)
print(answer)
    