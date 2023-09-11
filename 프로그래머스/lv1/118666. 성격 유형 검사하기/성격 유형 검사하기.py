def solution(survey, choices):
    find = ""
    choices = [i - 4 for i in choices]
    for num in range(len(survey)):
        if choices[num] < 0:
            find += survey[num][0] * -choices[num]
        else:
            find += survey[num][1] * choices[num]
    first = find.count("R") - find.count("T")
    second = find.count("C") - find.count("F")
    third = find.count("J") - find.count("M")
    forth = find.count("A") - find.count("N")
    
    count = [first, second, third, forth]
    mbti = ["RT", "CF", "JM", "AN"]
    answer = "" 
    for i in range(4):
        if count[i] >= 0:
            answer +=mbti[i][0]
        else:
            answer +=mbti[i][1]
    return answer