ans = 0
for _ in range(10):
    n = int(input())
    if n == 1:
        ans += 1
    elif n == 2:
        ans += 2
    else:
        ans -= 1
        
ans = ans % 4
dic = {0:'N', 1:'E', 2:'S', 3:'W'}
print(dic[ans])