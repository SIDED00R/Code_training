def check(n):
    if int(n ** 0.5) ** 2 == n:
        return True
    return False


n = int(input())
devided = []
for num in range(1, int(n ** 0.5) + 1):
    if n % num == 0:
        if (num + n // num) % 2 == 0:
            devided.append([num, n // num])
            
answer = 0
if check(n):
    print(-1)
    exit()
else:
    short_idx = 0
    squares = [i ** 2 for i in range(1, int((n / 2) ** 0.5 + 1))]
    for num in squares:
        if check(n - num):
            answer += 1 
            
print(answer + len(devided))
    
    
