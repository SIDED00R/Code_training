def solution(msg):
    dic = {chr(i + 65) : i + 1 for i in range(26)}
    word = ""
    answer = []

    for alp in msg:
        word += alp
        if word not in dic:
            dic[word] = len(dic) + 1
            answer.append(dic[word[:-1]])
            word = alp
    if word not in dic:
        answer.append(len(dic) + 1)
    else:
        answer.append(dic[word])
    return answer