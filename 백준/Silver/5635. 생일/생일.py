n = int(input())
birth = []
for _ in range(n):
    name, d, m, y = input().split()
    birth.append([int(y), int(m), int(d), name])
birth = sorted(birth)
print(birth[-1][-1])
print(birth[0][-1])