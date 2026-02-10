n = int(input())
line = list(input().split())
dic = {}
for i in range(n):
    dic[line[i]] = i
    
count = 0
answer = list(input().split())
for i in range(n):
    for j in range(i + 1, n):
        if dic[answer[i]] < dic[answer[j]]:
            count += 1
            
print(f"{count}/{n * (n - 1) // 2}")