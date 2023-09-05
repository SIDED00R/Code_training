def solution(arr, divisor):
    answer = []
    for num in arr:
        if num % divisor == 0:
            answer.append(num // divisor)
    answer = sorted(answer)
    return [n * divisor for n in answer] if answer != [] else [-1]