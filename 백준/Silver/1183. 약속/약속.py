n = int(input())
time_list = []
for _ in range(n):
    a, b = map(int, input().split())
    time_list.append(a - b)
time_list = sorted(time_list)
if n % 2 == 1:
    print(1)
else:
    mid = n // 2
    print(time_list[mid] - time_list[mid - 1] + 1)