n = int(input())
l = int(input())
c = int(input())

count = 1 + (c - l) // (l + 1)
if count % 13 == 0:
    count -= 1

answer = n // count
left = n % count

if answer == 0 and left % 13 == 0:
    print(2)
    exit()

if left != 0:
    answer += 1
    
    if left % 13 == 0:
        count -= 1
        left += 1
        if left > count:
            answer += 1
        elif count % 13 == 0:
            count -= 1
            left += 1
            if left > count:
                answer += 1

print(answer)
    
