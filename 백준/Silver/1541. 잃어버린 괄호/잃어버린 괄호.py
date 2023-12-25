import sys

input = sys.stdin.readline
line = input()

total = []
now_num = ""
for letter in line:
    if letter.isnumeric():
        now_num += letter
    elif letter == "+" or letter == "-":
        total.append(int(now_num))
        total.append(letter)
        now_num = ""
total.append(int(now_num))

answer = []
add_on = False
for num in total:
    if add_on:
        before = answer.pop()
        answer.append(before + num)
        add_on = False
    else:
        if num == "+":
            add_on = True
        else:
            answer.append(num)
      
if len(answer) == 1:
    print(answer[0])
else:
    ans = answer[0]
    rest = 0
    for num in answer[2:]:
        if num != "-":
            rest += num
    print(ans - rest)
