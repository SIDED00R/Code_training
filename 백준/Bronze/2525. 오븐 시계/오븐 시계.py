h, m = map(int, input().split())
add = int(input())
total = 60 * h + m + add
print((total // 60) % 24, total % 60)