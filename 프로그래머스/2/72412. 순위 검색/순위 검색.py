def solution(infos, queries):
    answer = []
    dic = {}

    for program in ['cpp', 'java', 'python', "-"]:
        for job in ['backend', 'frontend', "-"]:
            for career in ['junior', 'senior', "-"]:
                for food in ['chicken', 'pizza', "-"]:
                    dic[program + job + career + food] = []

    for info in infos:
        info = info.split()
        for program in [info[0], "-"]:
            for job in [info[1], "-"]:
                for career in [info[2], "-"]:
                    for food in [info[3], "-"]:
                        dic[program + job + career + food].append(int(info[4]))

    for key in dic.keys():
        dic[key].sort()

    for query in queries:
        query = query.replace("and", "").split()
        score = int(query[4])
        query = "".join(query[:4])

        info_score = dic[query]
        l = len(info_score)
        tmp = l

        low, high = 0, l - 1

        while low <= high:
            mid = (low + high) // 2

            if score <= info_score[mid]:
                tmp = mid
                high = mid - 1

            else:
                low = mid + 1

        answer.append(l - tmp)
    return answer