a, b = input().split()
al = len(a)
bl = len(b)
max_count = 10000000000
for i in range(bl - al + 1):
    count = 0
    for j in range(al):
        if a[j] != b[j + i]:
            count += 1
    max_count = min(count, max_count)
print(max_count)
        