from collections import defaultdict
dic = defaultdict(int)
line = input()
for alp in line:
    dic[alp] += 1
    
mid = ""
answer = ""
for k in sorted(dic):
    v = dic[k]
    if v % 2 == 0:
        answer += k * (v // 2)
    else:
        if mid == "":
            mid = k
            answer += k * ((v - 1) // 2)
        else:
            print("I'm Sorry Hansoo")
            exit()
            
print(answer + mid + answer[::-1])
    
