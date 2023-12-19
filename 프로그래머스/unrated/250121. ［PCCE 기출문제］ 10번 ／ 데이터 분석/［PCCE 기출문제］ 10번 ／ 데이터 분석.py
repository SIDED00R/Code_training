def solution(data, ext, val_ext, sort_by):
    dic = {"code":0, "date":1, "maximum":2, "remain":3}
    answer = []
    for case in data:
        if case[dic[ext]] < val_ext:
            answer.append(case)
    answer = sorted(answer, key = lambda x:x[dic[sort_by]])
    return answer