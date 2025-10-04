from collections import defaultdict

import sys
input = sys.stdin.readline

def able(dic1, dic2):
    for k, v in dic1.items():
        if dic1[k] > dic2[k]:
            return False
    return True

word_list = []
while True:
    word = input().rstrip('\n')
    d = defaultdict(int)
    if word == '-':
        break
    else:
        for alp in word:
            d[alp] += 1
        word_list.append(d)

while True:
    matrix = input().rstrip('\n')
    if matrix == '#':
        break
    answer = defaultdict(int)
    d = defaultdict(int)
    for alp in matrix:
        d[alp] += 1

    for now_d in word_list:
        if able(now_d, d):
            for k, v in now_d.items():
                answer[k] += 1
    min_count = 1e10
    max_count = 0
    min_set = set()
    max_set = set()
    for alp in matrix:
        now_count = answer[alp]
        if now_count > max_count:
            max_count = now_count
            max_set = set(alp)
        elif now_count == max_count:
            max_set.add(alp)

        if now_count < min_count:
            min_count = now_count
            min_set = set(alp)
        elif now_count == min_count:
            min_set.add(alp)
    print(f"{''.join(sorted(min_set))}", min_count, f"{''.join(sorted(max_set))}", max_count)
    