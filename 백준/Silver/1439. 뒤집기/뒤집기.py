import sys
input = sys.stdin.readline

before = ""
dic = {"1" : 0, "0" : 0}
for letter in input().rstrip('\n'):
    if before == "":
        before = letter
        dic[letter] += 1
    else:
        if before == letter:
            continue
        else:
            before = letter
            dic[letter] += 1
print(min(dic["1"], dic["0"]))