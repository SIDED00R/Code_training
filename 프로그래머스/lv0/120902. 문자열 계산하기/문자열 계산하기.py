def solution(my_string):
    
    
    
    letter = my_string.split()
    
    answer = int(letter[0])
    
    for i, n in enumerate(letter):
        if n == "+":
            answer += int(letter[i+1])
        elif n == "-":
            answer -= int(letter[i+1])
        
    return answer