from collections import Counter
n = int(input())
line = Counter(map(int, input().split()))
for k, v in line.items():
    if v % 2 == 1:
        print("koosaga")
        exit()
print("cubelover")