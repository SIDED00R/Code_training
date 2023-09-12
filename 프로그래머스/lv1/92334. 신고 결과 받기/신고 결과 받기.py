def solution(id_list, report, k):
    sumreport = [[] for _ in range(len(id_list))]
    for rep in set(report):
        user, ruser = rep.split()
        idx = id_list.index(ruser)
        sumreport[idx].append(user)
    
    result = [0 for _ in range(len(id_list))]
    for numreport in sumreport:
        if len(numreport) >= k:
            for memberid in numreport:
                idx = id_list.index(memberid)
                result[idx] += 1
            
    return result