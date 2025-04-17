n = int(input())
total_list = []
count = 0

one_dic = {0: "", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
ten_dic = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}
hund_dic = {1: "onehundred", 2: "twohundred", 3: "threehundred", 4: "fourhundred", 5: "fivehundred", 6: "sixhundred", 7: "sevenhundred", 8: "eighthundred", 9: "ninehundred"}
t = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
answer = {i + 10: t[i] for i in range(10)}
answer[0] = ""
for num in range(1, 1000):
    if num // 10 == 0:
        answer[num] = one_dic[num]
    elif num < 20:
        continue
    elif num // 100 == 0:
        ten = num // 10
        one = num % 10
        answer[num] = ten_dic[ten] + one_dic[one]
    else:
        hund = num // 100
        answer[num] = hund_dic[hund] + answer[num % 100]

for _ in range(n):
    line = input()
    if line != "$":
        count += len(line)
    total_list.append(line)

for num in range(1, 1000):
    able = answer[num]
    length = len(able)
    if num == count + length:
        ans = num
        break

for word in total_list:
    if word == "$":
        print(answer[ans], end = " ")
    else:
        print(word, end = " ")