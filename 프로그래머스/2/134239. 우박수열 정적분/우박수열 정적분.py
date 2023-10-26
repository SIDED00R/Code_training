def solution(k, ranges):
    sequence = [k]
    answer = []
    
    while k != 1:
        if k % 2 == 0:
            k //= 2
        else:
            k = k * 3 + 1
        sequence.append(k)
    
    for a, b in ranges:
        if b <= 0:
            b = len(sequence) - 1 + b
        if a == b:
            answer.append(0)
        elif a > b:
            answer.append(-1)
        else:
            total = 0
            for idx in range(a, b):
                total += (sequence[idx] + sequence[idx + 1]) / 2
            answer.append(total)

    return answer