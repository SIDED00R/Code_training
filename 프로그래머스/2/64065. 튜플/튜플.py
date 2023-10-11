def solution(s):
    length = s.count("},{") + 1
    
    case = [0 for _ in range(length)]
    
    count = 0
    ans = ""
    num = []
    for alp in s[:-1]:
        if alp == "{":
            count = 0
        elif alp.isnumeric():
            ans += alp
        elif alp == "," and ans != "":
            count += 1
            num.append(ans)
            ans = ""
        elif alp == "}":
            num.append(ans)
            case[count] = num[:]
            ans = ""
            num = []
            
    for i in range(len(case) - 1, 0, -1):
        for j in case[i - 1]:
            case[i].remove(j)
    
    
            
    return list(map(int,sum(case, [])))
    
