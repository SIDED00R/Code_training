from collections import Counter

def solution(strs, t):
    length = len(t)
    max_word_length = 0
    for s in strs:
        max_word_length = max(max_word_length, len(s))
    dp = [[1e9 for _ in range(max_word_length + 1)] for _ in range(length)]
    dic = Counter(strs)
    for i in range(length):
        for j in range(1, max_word_length + 1):
            if j > i:
                if t[:j] in dic:
                    dp[i][j] = 1
                break
            elif t[i + 1 - j:i + 1] in dic:
                dp[i][j] = min(dp[i - j]) + 1
    answer = min(dp[-1])
    if answer == 1e9:
        answer = -1
    return answer