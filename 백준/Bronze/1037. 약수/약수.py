n = int(input())
line = list(map(int, input().split()))
line.sort()
print(line[0] * line[-1])