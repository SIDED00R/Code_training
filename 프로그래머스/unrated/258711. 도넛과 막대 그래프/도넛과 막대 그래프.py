from collections import defaultdict
def solution(edges):
    dic = defaultdict(list)
    num = set()
    for edge in edges:
        a, b = edge
        dic[a].append(b)
        num.add(b)
        
    for key, value in dic.items():
        if key not in num:
            if len(dic[key]) > 1:
                answer_point = key
    donut = 0
    stick = 0
    eight = 0
    for case in dic[answer_point]:
        now = case
        while True:
            if now not in dic:
                stick += 1
                break
            elif len(dic[now]) == 2:
                eight += 1
                break
            else:
                now = dic[now][0]
                if now == case:
                    donut += 1
                    break
                
    return [answer_point, donut, stick, eight]