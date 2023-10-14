def perfect(s):
    count = 0
    able = []
    for bracket in s:
        if able == [] and (bracket == ")" or bracket == "]" or bracket == "}"):
            return False   
        
        elif bracket == ")":
            if able.pop() != "(":
                return False
            
        elif bracket == "]":
            if able.pop() != "[":
                return False
            
        elif bracket == "}":
            if able.pop() != "{":
                return False
            
        else:
            able.append(bracket)
        
        if len(able) == 0:
            count += 1
    
    if len(able) != 0:
        return False
    return count

def solution(s):
    s = list(s)
    for _ in range(len(s)): 
        if perfect(s):
            return perfect(s)
        else:
            right = s.pop()
            s = [right] + s
        
    return 0