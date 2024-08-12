
n = int(input())
start = 0
end = n
find = False
while start <= end:
    mid = (start + end) // 2
    if mid * (mid + 1) // 2 < n:
        start = mid + 1
    elif mid * (mid + 1) // 2 >= n:
        end = mid - 1
left = n - start * (start + 1) // 2
print(start ** 2 + 2 * left)
    