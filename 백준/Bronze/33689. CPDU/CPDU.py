n = int(input())
ans = 0
for _ in range(n):
    name = input()
    if name[0] == 'C':
        ans += 1
        
print(ans)