import sys
input = sys.stdin.readline

N = int(input())
arr = [0] * 101

for i in range(101):
    if i <= 3:
        arr[i] = 1
    elif i <= 5:
        arr[i] = 2
    else:
        arr[i] = arr[i - 1] + arr[i - 5]

for j in range(N):
    num = int(input())
    print(arr[num])

            
    
