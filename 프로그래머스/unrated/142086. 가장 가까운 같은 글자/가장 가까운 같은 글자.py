def solution(s):
    answer = []
    letter = ""
    for alp in s:
        if alp in letter:
            idx = letter.rindex(alp)
            difference = len(letter) - idx
            answer.append(difference)
        else:
            answer.append(-1)
        letter += alp
    return answer