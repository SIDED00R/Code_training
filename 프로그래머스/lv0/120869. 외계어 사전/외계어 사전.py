def solution(spell, dic):
    word = ''.join(sorted(spell))
    for w in dic:
        if ''.join(sorted(w)) == word:
            return 1
    return 2