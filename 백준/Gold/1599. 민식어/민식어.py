line = list("a b k d e g h i l m n ng o p r s t u w y".split())
dic = {line[i]: chr(97 + i) for i in range(20)}
rev_dic = {chr(97 + i): line[i] for i in range(20)}

n = int(input())
stack = []
for _ in range(n):
    word = input()
    change_word = ""
    idx = 0
    while idx != len(word):
        if idx < len(word) - 1 and word[idx: idx + 2] == "ng":
            change_word += dic["ng"]
            idx += 2
            continue
        change_word += dic[word[idx]]
        idx += 1

    stack.append(change_word)

stack.sort()

for word in stack:
    now_word = ""
    for alp in word:
        now_word += rev_dic[alp]
    print(now_word)