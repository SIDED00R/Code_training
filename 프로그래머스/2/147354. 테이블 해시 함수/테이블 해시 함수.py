def solution(data, col, row_begin, row_end):
    data = sorted(data, key = lambda x: [ x[col - 1], -x[0]])
    table = data[row_begin - 1:row_end]
    answer = []
    for idx, s in enumerate(table):
        total = 0
        for num in s:
            total += num % (idx + row_begin)
        answer.append(total)
    
    ans = 0
    for i in answer:
        ans = ans ^ i
    
    return ans