T = int(input())
paper = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(T):
    x, y = map(int, input().split())
    paper[x][y] += 1
    paper[x + 10][y] -= 1
    paper[x][y + 10] -= 1
    paper[x + 10][y + 10] += 1
    
for i in range(100):
    for j in range(100):
        paper[j + 1][i] += paper[j][i]
        
for i in range(100):
    for j in range(100):
        paper[i][j + 1] += paper[i][j]
        
answer = 0
for i in range(100):
    for j in range(100):
        if paper[i][j] != 0:
            answer += 1
            
print(answer)