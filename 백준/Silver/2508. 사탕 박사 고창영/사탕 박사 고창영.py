t = int(input())

for _ in range(t):
    blank = input()
    r, c = map(int, input().split())
    matrix = []
    answer = 0
    
    for _ in range(r):
        matrix.append(list(input()))
        
    for i in range(r):
        for j in range(c):
            if matrix[i][j] == "o":
                if 1 <= i < r - 1 and matrix[i - 1][j] == "v" and matrix[i + 1][j] == "^":
                    answer += 1
                elif 1 <= j < c - 1 and matrix[i][j - 1] == ">" and matrix[i][j + 1] == "<":
                    answer += 1 
    print(answer)