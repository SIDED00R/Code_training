from collections import defaultdict

def change(num, p):
    now_num = str(num)
    answer = 0
    for n in now_num:
        answer += int(n) ** p
    return answer

a, p = map(int, input().split())
dic = defaultdict(int)
while True:
    dic[a] += 1
    if dic[a] == 3:
        break
    else:
        a = change(a, p)
        
answer = 0
for k, v in dic.items():
    if v == 1:
        answer += 1
print(answer)
