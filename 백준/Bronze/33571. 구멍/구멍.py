one = 'AabDdegOoPpQqR@'
two = 'B'
line = input()
answer = 0
for alp in line:
    if alp in one:
        answer += 1
    elif alp in two:
        answer += 2
print(answer)