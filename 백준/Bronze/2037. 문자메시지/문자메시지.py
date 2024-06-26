dic = {}
check = 1
for i in range(26):
    alp = chr(i + 65)
    if alp == "A":
        check = 2
    elif alp == "D":
        check = 3
    elif alp == "G":
        check = 4
    elif alp == "J":
        check = 5
    elif alp == "M":
        check = 6
    elif alp == "P":
        check = 7
    elif alp == "T":
        check = 8
    elif alp == "W":
        check = 9
    dic[alp] = check
    
case = ["A", "D", "G", "J", "M", "P", "T", "W"]
p, w = map(int, input().split())
letter = input()
answer = 0
before = 0
for word in letter:
    if word == " ":
        answer += p
        before = 1
    else:
        check = dic[word]
        if before == check:
            answer += w
        before = check
        for idx in case:
            if dic[idx] == check:
                bottom = idx
                break
        answer += (ord(word) - ord(bottom) + 1) * p
        
print(answer)
        
    
