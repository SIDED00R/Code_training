def solution(begin, target, words):
    stack = [begin]
    n = len(begin)
    for i in range(len(words)):
        new_stack = []
        while stack:
            begin = stack.pop()
            for idx in range(len(words)):
                diff = 0
                word = words[idx]
                for j in range(n):
                    if word[j] != begin[j]:
                        diff += 1
                if diff == 1:
                    if word == target:
                        return i + 1
                    new_stack.append(word)
        for w in new_stack:
            words.remove(w)
        stack = new_stack[:]
        if stack == []:
            return 0
    return 0