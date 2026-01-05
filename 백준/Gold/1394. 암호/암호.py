dic = {}
line = input()
for idx, alp in enumerate(line):
    if alp not in dic:
        dic[alp] = idx + 1

answer = 0
find = input()
length = len(find)
for idx in range(length):
    answer += dic[find[idx]] * pow(len(line), (length - idx - 1), 900528)
print(answer % 900528)
    