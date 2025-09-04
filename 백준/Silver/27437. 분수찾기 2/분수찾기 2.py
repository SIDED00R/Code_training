n = int(input())
start = 1
end = int(1e18)
while start < end:
    mid = (start + end) // 2
    num = mid * (mid + 1) // 2
    if n > num:
        start = mid + 1
    else:
        end = mid

before = end * (end - 1) // 2
left = n - before
if end % 2 == 0:
    print(f"{left}/{end + 1 - left}")
else:
    print(f"{end + 1 - left}/{left}")
