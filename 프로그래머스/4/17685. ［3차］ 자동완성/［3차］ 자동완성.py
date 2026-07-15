def solution(words):
    sorted_words = sorted(words)
    same_count = [0]
    for i in range(1, len(words)):
        front = sorted_words[i - 1]
        back = sorted_words[i]
        count = 0
        for j in range(min(len(front), len(back))):
            if front[j] == back[j]:
                count += 1
            else:
                break
        same_count.append(count)
    same_count.append(0)
    answer = 0
    for i in range(1, len(words) + 1):
        answer += min(len(sorted_words[i - 1]), max(same_count[i - 1] + 1, same_count[i] + 1))
    return answer