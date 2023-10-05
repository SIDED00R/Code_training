def solution(citations):
    citations = sorted(citations, reverse = True)
    for idx in range(len(citations)):
        if idx < citations[idx]:
            continue
        else:
            return idx
        
    return len(citations)