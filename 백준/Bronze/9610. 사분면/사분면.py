n = int(input())
dic = {i:0 for i in range(5)}
for _ in range(n):
    x, y = map(int, input().split())
    if x == 0 or y == 0:
        dic[0] += 1
    elif x > 0 and y > 0:
        dic[1] += 1
    elif x > 0 and y < 0:
        dic[4] += 1
    elif x < 0 and y > 0:
        dic[2] += 1
    else:
        dic[3] += 1
        
for i in range(1, 5):
    print(f"Q{i}: {dic[i]}")
    
print(f"AXIS: {dic[0]}")