def solution(s):
    count = 0
    answer = 0
    
    while s != "1":
        count += 1
        num = s.count("1")
        answer += s.count("0")
        s = str(bin(num))[2:]
        
    return [count, answer]