n = int(input())
dic = {}
answer_list = []
for _ in range(n):
    line = list(input().split())
    find = False
    for idx, word in enumerate(line):
        first_letter = word[0].upper()
        if first_letter not in dic:
            find = True
            dic[first_letter] = 1
            line[idx] = f"[{word[0]}]{word[1:]}"
            answer_list.append(" ".join(line))
            break
    if find:
        continue
    else:
        total_word = " ".join(line)
        for idx in range(len(total_word)):
            now_letter = total_word[idx].upper()
            if now_letter == ' ':
                continue
            if now_letter not in dic:
                find = True
                dic[now_letter] = 1
                answer_list.append(f"{total_word[:idx]}[{total_word[idx]}]{total_word[idx + 1:]}")
                break
        if not find:    
            answer_list.append(total_word)

for l in answer_list:
    print(l)