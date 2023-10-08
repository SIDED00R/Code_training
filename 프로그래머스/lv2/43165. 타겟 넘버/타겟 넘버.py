def comb(arr ,n):

    ans = []

    if n == 0:
        return [[]]

    for i in range(len(arr)):
        element = arr[i]
        rest = arr[i + 1:]
        for j in comb(rest, n - 1):
            ans.append([element] + j)

    return ans

def solution(numbers, target):
    answer = 0
    total = sum(numbers)
    for i in range(len(numbers) + 1):
        for arr in comb(numbers, i):
            if total - sum(arr) * 2 == target:
                answer += 1
    return answer