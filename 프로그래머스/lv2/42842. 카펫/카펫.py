def solution(brown, yellow):
    total = brown + yellow
    cases = []
    for i in range(2, int(total ** 0.5) + 1):
        if total % i == 0:
            cases.append([total//i, i])
            
    for case in cases:
        if brown == sum(case) * 2 - 4:
            return case
