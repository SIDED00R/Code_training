def solution(n):
    num = list(str(n))
    num.sort(reverse = True)
    answer = "".join(num)    
    return int(answer)