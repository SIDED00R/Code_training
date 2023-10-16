def solution(numbers):
    answer = []
    for num in numbers:     
        b = bin(num)
        count = 0
        while True:
            if b[-1 - count] == "0" or b[-1 -count] == "b":
                break
            count += 1
        answer.append(num + 2**max(count - 1, 0))

    return answer
