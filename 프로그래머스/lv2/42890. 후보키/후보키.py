def findkey(relation, ableidx, checkidx, answer):

    if len(ableidx) == 0:
        return answer

    for i in range(len(ableidx)):
        keep = checkidx[:]
        idx = ableidx[i]
        checkidx.append(idx)
        rest = ableidx[i + 1:]

        arr = []
        for r in relation:
            line = []
            for c in checkidx:
                line.append(r[c])
            arr.append(line)
        arr = list(map(tuple, arr))
        
        if len(set(arr)) == len(arr):
            answer.append(checkidx[:])
            
        answer = findkey(relation, rest, checkidx, answer)
        checkidx = keep

    return answer


def solution(relation):
    relation = list(map(tuple, relation))
    ableidx = [i for i in range(len(relation[0]))]
    answer = findkey(relation, ableidx, [], [])
    
    new = []
    for item in answer:
        new.append(list(map(str,item)))
    new = list(map("".join, new))

    for i in range(len(new)):
        for j in range(len(new)):
            if i != j:
                added = True
                for num in new[i]:
                    if num in new[j]:
                        continue
                    else:
                        added = False
                        break
                if added:
                    new[j] = "no"
    return len(new) - new.count("no")