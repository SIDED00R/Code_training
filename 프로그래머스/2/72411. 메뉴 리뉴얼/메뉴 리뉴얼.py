def make_combination(letter, n):
    comb = []
    if n == 0:
        return [[]]

    for i in range(len(letter)):
        now = letter[i]
        rest = letter[i + 1:]
        for j in make_combination(rest, n - 1):
            comb.append(now + "".join(j))
    return comb

def make_course(orders, num):
    cases = []
    dic = {}
    for order in orders:
        order = sorted(list(order))
        cases += make_combination(order, num)
    for case in cases:
        if case in dic:
            dic[case] += 1
        else:
            dic[case] = 1
    return dic
    
def solution(orders, course):
    answer = []
    for num in course:
        min_num = 2
        possible = []
        for key, value in make_course(orders, num).items():
            if value == min_num:
                possible.append(key)
            elif value > min_num:
                min_num = value
                possible = [key]
        answer += possible
        
    return sorted(answer)