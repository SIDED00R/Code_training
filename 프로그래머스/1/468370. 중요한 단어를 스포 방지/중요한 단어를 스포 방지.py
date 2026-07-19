def solution(message, spoiler_ranges):
    answer = 0
    
    message += " "
    dic = {}
    now_word = ""
    secrete = False
    spoiler_ranges.append([1e9, 1e9])
    now_range = 0
    for idx in range(len(message)):
        now = message[idx]
        if now == " ":
            if secrete and now_word not in dic:
                dic[now_word] = 1
                answer += 1
            elif not secrete and now_word not in dic:
                dic[now_word] = 0
            elif not secrete and now_word in dic and dic[now_word] == 1:
                dic[now_word] = 0
                answer -= 1
            secrete = False
            now_word = ""
        else:
            while spoiler_ranges[now_range][1] < idx:
                now_range += 1
            start, end = spoiler_ranges[now_range]
            if start <= idx <= end:
                secrete = True
            now_word += message[idx]
    
    return answer