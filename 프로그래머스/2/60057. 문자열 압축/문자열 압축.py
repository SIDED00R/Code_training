def solution(s):
    answer = []
    for i in range(1, len(s) // 2 + 1):
        ans = ""
        count = 0
        now = s[:i]
        startidx = list(range(0, len(s), i))
        
        for j in startidx:
            if now == s[j:j + i]:
                count += 1
            else:
                if count == 1:
                    ans += now
                else:
                    ans = ans + f"{count}" + now
                    count = 1
                now = s[j:j + i]
        if count > 1:
            ans = ans + f"{count}" + now
        else:
            ans += now
        answer.append(ans)

    minnum = len(s)
    
    for short in answer:
        if len(short) < minnum:
            minnum = len(short)
    
    return minnum