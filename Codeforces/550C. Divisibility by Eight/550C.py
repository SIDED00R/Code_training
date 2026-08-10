from itertools import combinations

answer = -1
n = input()

if "8" in n:
    answer = 8
elif "0" in n:
    answer = 0
    
if len(n) >= 2:
    for now_case in combinations(n, 2):
        now_case = "".join(now_case)
        if int(now_case) % 8 == 0:
            answer = max(answer, int(now_case))    
if len(n) >= 3:
    for now_case in combinations(range(len(n)), 3):
        a, b, c = now_case
        if int(n[a] + n[b] + n[c]) % 8 == 0:
            answer = max(answer, int(n[:0] + n[a] + n[b] + n[c]))

if answer == -1:
    print("NO")
else:
    print("YES")
    print(answer)