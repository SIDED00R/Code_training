def solution(food):
    answer = ""
    for num in range(1, len(food)):
        able = food[num] // 2
        answer += f"{num}" * able
    return answer + "0" + answer[::-1]