able = [1]
num = 1
for i in range(1, 20):
    num *= i
    able.append(num)
    
n = int(input())
if n == 0:
    print("NO")
    exit()
while able:
    if able[-1] > n:
        able.pop()
    else:
        n -= able.pop()
        
if n == 0:
    print("YES")
else:
    print("NO")



