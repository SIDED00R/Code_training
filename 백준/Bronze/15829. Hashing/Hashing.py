import sys

n = int(sys.stdin.readline())

word = sys.stdin.readline()
dic = {chr(i + 97): i + 1 for i in range(26)}

answer = 0

for i in range(n):
    answer += (dic[word[i]] * (31 ** i)) % 1234567891
print(answer)
