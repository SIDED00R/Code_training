def solution(priorities, location):
    total = len(priorities)
    loc = [0 for _ in range(total)]
    loc[location] = 1
    
    while True:
        
        idx = priorities.index(max(priorities))
        if loc[idx] == 1:
            break
            
        priorities = priorities[idx + 1:] + priorities[:idx]
        loc = loc[idx + 1:] + loc[:idx]

    return total - len(loc) + 1