n = int(input())
if n % 2 == 0 or n % 5 == 0:
    print(-1)
    exit()
count = 1
left = 1
while True:
    left = left % n
    if left == 0:
        break
    count += 1
    left = left * 10 + 1
print(count)