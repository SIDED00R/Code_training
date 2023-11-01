def solution(storey):
    numbers = list(map(int, list(str(storey))))
    answer = 0
    upper = 0
    for i in range(len(numbers) - 1, 0, -1):
        if numbers[i] + upper < 5:
            answer += numbers[i] + upper
            upper = 0
        elif numbers[i] + upper > 5:
            answer += 10 - numbers[i] - upper
            upper = 1
        else:
            if numbers[i - 1] >= 5:
                answer += 10 - numbers[i] - upper
                upper = 1
            else:
                answer += numbers[i] + upper
                upper = 0
    
    if numbers[0] + upper > 5:
        return answer + 10 - numbers[0] - upper + 1
    else:
        return answer + numbers[0] + upper