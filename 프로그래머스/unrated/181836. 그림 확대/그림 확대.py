def solution(picture, k):
    answer = []
    for pix in picture:
        line = ""
        for dot in pix:
            line += dot * k
        for _ in range(k):
            answer.append(line)
    return answer