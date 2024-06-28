n = int(input())
count = 1
answer = 0
while n != 0:
    left = n % 10
    if left > 4:
        answer += count * (left - 1)
    else:
        answer += count * left
    n //= 10
    count *= 9
    
print(answer)
    