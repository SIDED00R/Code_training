min_num, max_num = map(int, input().split())
length = max_num - min_num + 1
check = [1 for _ in range(length)]

end = int(max_num ** 0.5) + 1

for num in range(2, end):
    now = num ** 2
    start = min_num % now
    if start != 0:
        start = now - start
    for idx in range(start, length, now):
        check[idx] = 0

print(sum(check))
