dic = {}
for i in range(26):
    dic[chr(97 + i)] = 0

n = int(input())
line = input()

count = 0
answer = 0
now_answer = 0
pointer = 0
for alp in line:
    if dic[alp] == 0:
        count += 1
    now_answer += 1
    dic[alp] += 1
    while count > n:
        p_alp = line[pointer]
        pointer += 1
        dic[p_alp] -= 1
        now_answer -= 1
        if dic[p_alp] == 0:
            count -= 1
    answer = max(answer, now_answer)

print(answer)
    
            