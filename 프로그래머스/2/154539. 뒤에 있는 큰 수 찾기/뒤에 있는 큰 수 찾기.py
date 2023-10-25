def solution(numbers):
    stack = []
    answer = [-1] * len(numbers)
    for idx, num in enumerate(numbers):
        while stack != []:
            i, n = stack[-1]
            if n < num:
                stack.pop()
                answer[i] = num
            else:
                break
        stack.append([idx, num])
    return answer

