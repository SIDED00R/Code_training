def solution(score):
    total = [sum(i) for i in score]
    answer = [0 for _ in range(len(score))]
    number = sorted(set(total))
    rank = 1
    same = 0
    print(number, total)   
    for num in number[::-1]:
        for idx, n in enumerate(total):
            if n == num:
                answer[idx] = rank
                same += 1
        rank += same
        same = 0
        
    return answer