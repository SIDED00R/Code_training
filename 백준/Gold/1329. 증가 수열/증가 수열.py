from collections import deque
import sys

s = list(sys.stdin.readline().strip())
n = len(s)

MAX = 81
terms = [[0, 0] for _ in range(MAX)]

minTerm = [0, n - 1]
minSequence = [[0, n - 1]]

def get_term(term):
    res = []
    i, j = term
    for k in range(i, j + 1):
        res.append(s[k])
    return "".join(res)

def compare(term1, term2):
    s1, e1 = term1
    s2, e2 = term2
    while s1 <= e1 and s[s1] == '0':
        s1 += 1
    while s2 <= e2 and s[s2] == '0':
        s2 += 1
    len1 = e1 - s1 + 1
    len2 = e2 - s2 + 1
    if len1 < len2:
        return -1
    elif len1 > len2:
        return 1
    for i in range(len1):
        d1 = ord(s[s1 + i]) - 48
        d2 = ord(s[s2 + i]) - 48
        if d1 != d2:
            return -1 if d1 < d2 else 1
    return 0

def deep_copy(seq):
    return [[a, b] for (a, b) in seq]

def is_better(candidate):
    global minSequence
    cand_size = len(candidate)
    min_size = len(minSequence)
    size = min(cand_size, min_size)
    for idx, cand_term in enumerate(candidate):
        if idx == size:
            break
        comp = compare(cand_term, minSequence[idx])
        if comp > 0:
            return True
        elif comp < 0:
            return False
    return cand_size > min_size

def backtracking(nth, idx, sequence):
    global minTerm, minSequence
    if idx == n:
        cmpv = compare(terms[nth - 1], minTerm)
        if cmpv < 0:
            minTerm[0], minTerm[1] = terms[nth - 1][0], terms[nth - 1][1]
            minSequence = deep_copy(sequence)
        elif cmpv == 0:
            if is_better(sequence):
                minTerm[0], minTerm[1] = terms[nth - 1][0], terms[nth - 1][1]
                minSequence = deep_copy(sequence)
        return

    if nth == 0:
        for end in range(idx, n):
            terms[nth][0] = idx
            terms[nth][1] = end
            terms[nth + 1][0] = end + 1
            sequence.append((terms[nth][0], terms[nth][1]))
            backtracking(nth + 1, end + 1, sequence)
            sequence.pop()
    else:
        smaller = True
        terms[nth][0] = idx
        for end in range(idx, n):
            terms[nth][1] = end
            if smaller and compare(terms[nth - 1], terms[nth]) >= 0:
                continue
            if compare(minTerm, terms[nth]) < 0:
                return
            smaller = False
            terms[nth + 1][0] = end + 1
            sequence.append((terms[nth][0], terms[nth][1]))
            backtracking(nth + 1, end + 1, sequence)
            sequence.pop()

backtracking(0, 0, deque())

out = []
for i, term in enumerate(minSequence):
    out.append(get_term(term))
print(",".join(out))
