def solution(s, skip, index):
    able = [1 for _ in range(26)]
    letter = ""
    for alp in skip:
        able[ord(alp) - 97] = 0
    for idx, num in enumerate(able):
        if num:
            letter += chr(idx + 97)
    
    letter *= 3
    
    answer = ""
    for alp in s:
        idx = letter.index(alp)
        answer += letter[idx + index]
    return answer