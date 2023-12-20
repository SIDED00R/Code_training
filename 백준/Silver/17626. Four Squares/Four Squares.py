import sys
input = sys.stdin.readline

arr = [5] * 50001
for i in range(50001):
    mid = int(i ** 0.5)
    if i <= 1:
        arr[i] = 1
    elif mid ** 2 == i:
        arr[i] = 1
    else:
        for j in range(1, mid + 1):
            now = i
            now -= j ** 2
            if arr[i] > arr[now] + 1:
                arr[i] = arr[now] + 1
N = int(input())
print(arr[N])



