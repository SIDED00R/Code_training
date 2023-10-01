def base(n, num):
    over = ["A","B","C","D","E","F"]
    answer = ""
    if num == 0:
        return "0"
    while num != 0:
        if num % n >= 10:
            answer += over[num % n -10]
        else:
            answer += str(num % n)
        num //= n
    return answer[::-1]
    

def solution(n, t, m, p):
    word = ""
    idx = [p + m * i - 1 for i in range(t)]
    for i in range(m * t):
        word += base(n, i)
    
    
    return "".join([word[i] for i in idx])