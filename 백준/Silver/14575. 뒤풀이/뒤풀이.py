n, t = map(int, input().split())
min_value = []
max_value = []
for _ in range(n):
    l, r = map(int, input().split())
    min_value.append(l)
    max_value.append(r)

low = max(min_value)
high = max(max_value)

if sum(min_value) <= t <= sum(max_value):
    while low < high:
        mid = (low + high) // 2
        new_high = []
        for num in max_value:
            new_high.append(min(num, mid))
        if t <= sum(new_high):
            high = mid - 1
        else:
            low = mid + 1
    print(low)
else:
    print(-1)