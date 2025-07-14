answer = 0
for _ in range(4):
    answer += int(input())
    
if answer + 300 <= 1800:
    print('Yes')
else:
    print('No')