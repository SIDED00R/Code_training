def solution(number, k):
    number = list(number)
    answer = []
    finish = False
    for num in number:
        while not finish and len(answer) != 0 and num > answer[-1]:
            answer.pop()
            k -= 1
            if k == 0:
                finish = True
                break
        answer.append(num)
    
    if k:
        for i in range(k):
            answer.pop()
    
    return "".join(answer)