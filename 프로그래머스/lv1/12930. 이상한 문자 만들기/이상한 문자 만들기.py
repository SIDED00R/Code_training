def solution(s):
    s = list(s.upper())
    i = 0
    for idx, alp in enumerate(s):
        if alp == " ":
            i = 0
            continue
        else:
            if i % 2 == 1:
                s[idx] = s[idx].lower()
            i += 1
            
            
    return "".join(s)