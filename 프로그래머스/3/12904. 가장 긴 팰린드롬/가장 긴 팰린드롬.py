def solution(s):
    answer = 0
    if len(s) == 1:
        return 1
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            count = 1
            while True:
                if not (i - count < 0 or i + 1 + count >= len(s)) and s[i - count] == s[i + 1 + count]:
                    count += 1
                else:
                    break
            if answer < count * 2:
                answer = count * 2
                
        count = 1
        while True:
            if not (i - count < 0 or i + count >= len(s)) and s[i - count] == s[i + count]:
                count += 1
            else:
                break
        if answer < count * 2 - 1:
            answer = count * 2 - 1
            
    return answer