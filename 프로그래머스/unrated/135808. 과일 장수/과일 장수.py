def solution(k, m, score):
    many = []
    answer = 0
    left = 0
    for num in range(1, k + 1):
        many.append(score.count(num))
    for n in range(k, 0, -1):
        answer += ((many[n - 1] + left) // m) * n * m
        left = (many[n - 1] + left) % m
    return answer