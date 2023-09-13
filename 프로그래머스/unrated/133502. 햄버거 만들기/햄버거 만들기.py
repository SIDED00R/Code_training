def solution(ingredient):
    stack = []
    answer = 0
    for ingred in ingredient:
        stack.append(ingred)
        if stack[-4:] == [1, 2, 3, 1]:
            for _ in range(4):
                stack.pop()
            answer += 1
    return answer