from collections import defaultdict
n = int(input())
dic = defaultdict(int)
for _ in range(n):
    for num in list(map(int, input().split())):
        dic[num] += 1
        if dic[num] == 2:
            print(1)
            exit()
print(0)
