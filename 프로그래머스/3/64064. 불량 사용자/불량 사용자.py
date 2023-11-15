from itertools import permutations

def solution(user_id, banned_id):
    answer = []
    data = permutations(user_id, len(banned_id))
    for line in data:
        find = True
        for word in range(len(line)):
            if len(line[word]) != len(banned_id[word]):
                find = False
                break
            for alp in range(len(line[word])):
                if line[word][alp] == banned_id[word][alp] or banned_id[word][alp] == "*":
                    continue
                else:
                    find = False
                    break
            if find:
                continue
            else:
                break
        if find:
            answer.append(line)
        else:
            continue
    sort_answer = []
    for line in answer:
        line = tuple(sorted(line))
        sort_answer.append(line)
    ans = set(sort_answer)
    return len(ans)