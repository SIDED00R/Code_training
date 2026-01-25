n, k = map(int, input().split())
letter = input()
dic = {chr(97 + i): 0 for i in range(26)}
for alp in letter:
    dic[alp] += 1

min_value = 1e10
for _, v in dic.items():
    min_value = min(min_value, v)

if k < min_value:
    print(0)
else:
    print(1)