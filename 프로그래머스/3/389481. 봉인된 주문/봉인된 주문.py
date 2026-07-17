dic = {chr(97 + i):i + 1 for i in range(26)}

def solution(n, bans):
    bans_num = []
    for ban in bans:
        length = len(ban) - 1
        num = 0
        for letter in ban:
            num += dic[letter] * (26 ** length)
            length -= 1
        bans_num.append(num)
    bans_num = sorted(bans_num)
    for now_num in bans_num:
        if now_num <= n:
            n += 1
    answer = ""
    while n:
        now = chr(97 + (n - 1) % 26)
        answer = now + answer
        n = (n - 1) // 26
    return answer