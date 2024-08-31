n = int(input())
line = map(int, input().split())
y, m = 0, 0
for num in line:
    y += (num // 30 + 1) * 10
    m += (num // 60 + 1) * 15
if y < m:
    print(f"Y {y}")
elif m < y:
    print(f"M {m}")
else:
    print(f"Y M {y}")