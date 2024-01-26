import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
line = input().rstrip('\n').split("O")
count = 0
answer = 0
for num in line:
    if num == "I":
        if count == N:
            answer += 1
        else:
            count += 1
    elif num != "":
        if count == N:
            answer += 1
            count = 1
        else:
            count = 1
    else:
        count = 0
print(answer)

  
