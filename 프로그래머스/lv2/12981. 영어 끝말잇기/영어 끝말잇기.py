def solution(n, words):
    start = words[0]
    said = [start]
    wrong = False
    
    for idx, word in enumerate(words[1:]):
        if said[-1][-1] != word[0]:
            wrong = True
            i = idx + 1
            break
        elif word in said:
            wrong = True
            i = idx + 1
            break
        else:
            said.append(word)
            
    if wrong:
        return [i % n + 1 , i // n + 1]
        
    else:
        return [0, 0]
        
        
    return answer