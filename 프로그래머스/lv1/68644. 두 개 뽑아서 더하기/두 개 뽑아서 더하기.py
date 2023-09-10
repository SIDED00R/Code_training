def solution(numbers):
    answer = set()
    for idx, i in enumerate(numbers[:-1]):
        for j in numbers[idx + 1:]:
            answer.add(i + j)
    return sorted(answer)