def check(num):
    total = 0
    count = 0
    for i in range(1, num + 1):
        if count + i <= num:
            count += i
            total += i * i
        else:
            diff = num - count
            total += diff * i
            break
    return total

a, b = map(int, input().split())
print(check(b) - check(a - 1))