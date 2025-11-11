def find(idx):
    while num[0][idx] != "*":
        idx += 1
    if (num[0][idx:idx + 3] == "***") and (num[1][idx:idx + 3] == "* *") and (num[2][idx:idx + 3] == "* *") and (num[3][idx:idx + 3] == "* *") and (num[4][idx:idx + 3] == "***"):
        answer = 0
    elif (num[0][idx:idx + 2] == "* ") and (num[1][idx:idx + 2] == "* ") and (num[2][idx:idx + 2] == "* ") and (num[3][idx:idx + 2] == "* ") and (num[4][idx:idx + 2] == "* "):
        answer = 1
        idx -= 2
    elif (num[0][idx:idx + 3] == "***") and (num[1][idx:idx + 3] == "  *") and (num[2][idx:idx + 3] == "***") and (num[3][idx:idx + 3] == "*  ") and (num[4][idx:idx + 3] == "***"):
        answer = 2
    elif (num[0][idx:idx + 3] == "***") and (num[1][idx:idx + 3] == "  *") and (num[2][idx:idx + 3] == "***") and (num[3][idx:idx + 3] == "  *") and (num[4][idx:idx + 3] == "***"):
        answer = 3
    elif (num[0][idx:idx + 3] == "* *") and (num[1][idx:idx + 3] == "* *") and (num[2][idx:idx + 3] == "***") and (num[3][idx:idx + 3] == "  *") and (num[4][idx:idx + 3] == "  *"):
        answer = 4
    elif (num[0][idx:idx + 3] == "***") and (num[1][idx:idx + 3] == "*  ") and (num[2][idx:idx + 3] == "***") and (num[3][idx:idx + 3] == "  *") and (num[4][idx:idx + 3] == "***"):
        answer = 5
    elif (num[0][idx:idx + 3] == "***") and (num[1][idx:idx + 3] == "*  ") and (num[2][idx:idx + 3] == "***") and (num[3][idx:idx + 3] == "* *") and (num[4][idx:idx + 3] == "***"):
        answer = 6
    elif (num[0][idx:idx + 3] == "***") and (num[1][idx:idx + 3] == "  *") and (num[2][idx:idx + 3] == "  *") and (num[3][idx:idx + 3] == "  *") and (num[4][idx:idx + 3] == "  *"):
        answer = 7
    elif (num[0][idx:idx + 3] == "***") and (num[1][idx:idx + 3] == "* *") and (num[2][idx:idx + 3] == "***") and (num[3][idx:idx + 3] == "* *") and (num[4][idx:idx + 3] == "***"):
        answer = 8
    elif (num[0][idx:idx + 3] == "***") and (num[1][idx:idx + 3] == "* *") and (num[2][idx:idx + 3] == "***") and (num[3][idx:idx + 3] == "  *") and (num[4][idx:idx + 3] == "***"):
        answer = 9
    else:
        answer = -1
        
    idx += 3
    return idx, answer

num = []
for _ in range(5):
    line = input() + " "
    num.append(line)

answer = 0
idx = 0
while idx < len(num[0]) - 1:
    idx, number = find(idx)
    if number == -1:
        print("BOOM!!")
        exit()
    else:
        answer *= 10
        answer += number

if answer % 6 == 0:
    print("BEER!!")
else:
    print("BOOM!!")