import sys
input = sys.stdin.readline

N = int(input())

metrix = []
for _ in range(N):
    line = list(map(int, input().split()))
    metrix.append(line)

zero = 0
one = 0
for i in range(N):
    for j in range(N):
        if metrix[i][j] == 0:
            zero += 1
        else:
            one += 1
 
count = 1
while count != N:
    count *= 2
    check_zero = 0
    check_one = 0
    for i in range(N // count):
        for j in range(N // count):
            if metrix[i * count][j * count] + metrix[i * count + count // 2][j * count] + metrix[i * count][j * count + count // 2] + metrix[i * count + count // 2][j * count + count // 2] == 0:
                check_zero += 1
            elif metrix[i * count][j * count] + metrix[i * count + count // 2][j * count] + metrix[i * count][j * count + count // 2] + metrix[i * count + count // 2][j * count + count // 2] == 4:
                check_one += 1
            else:
                metrix[i * count][j * count] = 1000
    zero -= check_zero * 3
    one -= check_one * 3
print(zero)
print(one)