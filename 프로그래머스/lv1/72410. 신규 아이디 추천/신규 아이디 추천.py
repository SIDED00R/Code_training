def solution(new_id):
    answer = ""
    for letter in new_id:
        if letter.isalpha():
            answer += letter.lower()
        elif letter == ".":
            if answer == "":
                continue
            if answer[-1] == ".":
                continue
            else:
                answer += letter
        elif letter in ["-", "_"]:
            answer += letter
        elif letter.isdigit():
            answer += letter
    while len(answer) > 1 and answer[-1] == ".":
        answer = answer[:-1]
    if answer == ".":
        answer = ""
    if answer == "":
        answer = "a"
    if len(answer) >= 16:
        answer = answer[:15]
        while answer[-1] == ".":
            answer = answer[:-1]
    while len(answer) <= 2:
        answer += answer[-1]  
        
    return answer
