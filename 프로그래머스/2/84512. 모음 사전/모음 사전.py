def solution(word):
    answer = 0
    vowel = ["A", "E", "I", "O", "U"]
    num = [781, 156, 31, 6, 1]
    for i in range(len(word)):
        answer += vowel.index(word[i]) * num[i] + 1
    return answer