import sys
input = sys.stdin.readline

s = input().rstrip()
able = []

for idx in range(1, len(s) + 1):
    if s[:idx] == s[-idx:]:
        able.append(s[-idx:])

find = False
for now_case in able[::-1]:
    if now_case in s[1:-1]:
        find = True
        answer = now_case
        break

if find:
    print(answer)
else:
    print("Just a legend")