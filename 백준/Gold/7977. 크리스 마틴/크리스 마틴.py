dic = {"A":0, "C":0, "G":0, "T":0}
n = int(input())
line = list(input())
for word in line:
    dic[word] += 1

answer = ""
c = n

for k, v in dic.items():
    if v < c:
        answer = k
        c = v

print(c)
print(answer * n)