n = int(input())
line = list(map(int, input().split()))
line.sort()
x = int(input())

front = 0
back = n - 1
answer = 0
while front < back:
    now_x = line[front] + line[back]
    if x == now_x:
        answer += 1
        front += 1
        back -= 1
    elif x > now_x:
        front += 1
    else:
        back -= 1
        
print(answer)