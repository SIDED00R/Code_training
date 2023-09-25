def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    
    stack = []
    answer = 0
    
    for city in cities:
        
        c = city.lower()
        
        if c in stack:
            answer += 1
            stack.pop(stack.index(c))
            stack.append(c)
            
        elif len(stack) < cacheSize:
            answer += 5
            stack.append(c)
            
        else:
            answer += 5
            stack.pop(0)
            stack.append(c)
    
        
    return answer