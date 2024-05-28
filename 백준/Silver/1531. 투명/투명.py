N, M = map(int, input().split())
picture = [[0 for _ in range(101)] for _ in range(101)]
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    picture[x1 - 1][y1 - 1] += 1
    picture[x1 - 1][y2] -= 1
    picture[x2][y1 - 1] -= 1
    picture[x2][y2] += 1
    
for i in range(101):
    for j in range(100):
        picture[i][j + 1] += picture[i][j]
  
        
for i in range(100):
    for j in range(101):
        picture[i + 1][j] += picture[i][j]
    
        
count = 0
for i in range(100):
    for j in range(100):
        if picture[i][j] > M:
            count += 1
            
print(count)