def solution(elements):
    answer = set()
    new = elements * 2
    for i in range(1, len(elements) + 1):
        for j in range(len(elements)):
            answer.add(sum(new[j:j + i]))
    return len(answer)