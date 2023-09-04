def solution(arr, k):
    answer = [-1 for _ in range(k)]
    i = 0
    for num in arr:
        if num not in answer:
            answer[i] = num
            i += 1
        if i == k:
            return answer
    return answer