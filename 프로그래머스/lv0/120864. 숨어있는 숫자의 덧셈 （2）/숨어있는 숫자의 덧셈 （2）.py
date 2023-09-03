def solution(my_string):
    num = "0"
    answer = 0
    for l in my_string:
        if l.isnumeric():
            num += l
        else:
            answer += int(num)
            num = "0"
    
    return answer + int(num)