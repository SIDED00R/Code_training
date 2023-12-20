import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
sum_arr = []
total = 0
for num in arr:
    total += num
    sum_arr.append(total)
for _ in range(M):
    i, j = map(int, input().split())
    if i != 1:
        print(sum_arr[j - 1] - sum_arr[i - 2])
    else:
        print(sum_arr[j - 1])

