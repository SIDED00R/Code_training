n = int(input())
l = []
for _ in range(n):
    price = int(input())
    l.append(price)
    
m = int(input())
answer = 0
for _ in range(m):
    answer += l[int(input()) - 1]
    
print(answer)