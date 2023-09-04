def solution(myString, pat):
    idx = []
    for i in range(len(myString) - len(pat) + 1):
        if myString[i : i + len(pat)] == pat:
            idx.append(i)
    
    return myString[:idx[-1] + len(pat)]