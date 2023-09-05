def solution(babbling):
    answer = 0
    case = ["aya", "ye", "woo", "ma" ]
    fcase = [word * 2 for word in case]
    
    for word in babbling:
        bab = ""
        babb = ""
        for alp in word:
            bab += alp
            if bab in case:
                if babb == bab:
                    break
                babb = bab
                bab = ""
        if bab == "":
            answer += 1
            
    return answer