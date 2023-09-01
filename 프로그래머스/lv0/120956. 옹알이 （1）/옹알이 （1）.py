def solution(babbling):
    answer = 0
    case = ["aya", "ye", "woo", "ma" ]
    
    
    for sample in babbling:
        count = 0
        while sample != "":
            for i in case:
                if sample.startswith(i):
                    sample = sample.replace(i,"")
                    print(sample)
                if sample == "":
                    answer += 1
                    break
            count += 1
            if count > 5:
                break
            
                
    
    return answer