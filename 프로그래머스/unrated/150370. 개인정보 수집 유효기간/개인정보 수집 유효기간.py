def solution(today, terms, privacies):
    year, month, day = today.split(".")
    today = year + month + day
    dic = {}
    answer = []
    
    for term in terms:
        ty, length = term.split()
        dic[ty] = int(length)
    
    for idx, privacie in enumerate(privacies):
        date, types = privacie.split()
        dyear, dmonth, dday = map(int, date.split("."))
        
        length = dic[types]
        lyear = length // 12
        lmonth = length % 12
        dyear += lyear
        dmonth += lmonth
        dday -= 1
        
        if dday == 0:
            dday = 28
            dmonth -= 1
        
        if dmonth == 0:
            dmonth = 12
            dyear -= 1
        elif dmonth > 12:
            dmonth = dmonth % 12
            dyear += 1
        
        if dmonth < 10:
            dmonth = f"0{dmonth}"
            
        if dday < 10:
            dday = f"0{dday}"
            
        finalday = f"{dyear}{dmonth}{dday}"
        print(finalday, today)
        if today > finalday:
            answer.append(idx + 1)
    return answer