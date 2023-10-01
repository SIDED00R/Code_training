def solution(files):
    answer = []
    for file in files:
        head = ""
        number = ""
        tail = ""
        
        for alp in file:
            
            if len(number) == 0:
                if not alp.isnumeric():
                    head += alp
                else:
                    number += alp
            elif len(tail) == 0:
                if alp.isnumeric():
                    number += alp
                else:
                    break
                    
        answer.append([file, head.lower(), int(number)])
                
    answer = sorted(answer, key = lambda x : (x[1], x[2]))        
    return [i[0] for i in answer]