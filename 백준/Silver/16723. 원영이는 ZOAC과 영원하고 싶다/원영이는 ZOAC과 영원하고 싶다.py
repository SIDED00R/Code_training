n = int(input())

find = 1
while find <= n:
    find *= 2
find //= 2

answer = 0
count = 0
while find != 1:
    for num in range(1, n, 2):
        if find * num > n:
            break
        else:
            answer += find
            count += 1
    find //= 2
    
print(2 * (answer + n - count))
