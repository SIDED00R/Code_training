def findword(string, stack):
    before = ""
    for alp in string.lower():
        if not alp.isalpha():
            before = ""
            continue
        elif before == "":
            before = alp
        else:
            stack.append(before + alp)
            before = alp
    return stack

def solution(str1, str2):
    s1 = []
    s2 = []
    s1 = findword(str1, s1)
    s2 = findword(str2, s2)
    
    if len(s1) + len(s2) == 0:
        return 65536
    elif len(s1) == 0 or len(s2) == 0:
        return 0
    
    count = 0
    for word in set(s1):
        if word in s2:
            count += min(s1.count(word), s2.count(word))
            
    total = len(s1) + len(s2) - count 
    
    return int(65536 * count / total)