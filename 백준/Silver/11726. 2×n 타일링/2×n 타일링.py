import sys
input = sys.stdin.readline

arr = [0] * 1001
for i in range(1001):
    if i <= 1:
        arr[i] = 1
    else:
        arr[i] = arr[i - 1] + arr[i - 2]
N = int(input())
print(arr[N]%10007)



