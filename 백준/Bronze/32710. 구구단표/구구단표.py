dic = {}
for i in range(1, 10):
    for j in range(i, 10):
        dic[i * j] = 1

n = int(input())
if n in dic:
    print(1)
else:
    print(0)