from collections import defaultdict

def solution(coin, cards):
    n = len(cards)
    key = n + 1
    open_dic = defaultdict(int)
    pair_num = 1
    check = n // 3
    
    for num in cards[:check]:
        if (key - num) in open_dic:
            del(open_dic[key - num])
            pair_num += 1
        else:
            open_dic[num] = 1
            
    trash_dic = defaultdict(int)
    trash_pair = 0
    while pair_num != 0:
        if check == n:
            return (check - n // 3) // 2 + 1
        pair_num -= 1
        for num in cards[check:check + 2]:
            if coin == 0:
                continue
            else:
                if (key - num) in open_dic:
                    del(open_dic[key - num])
                    coin -= 1
                    pair_num += 1
                elif (key - num) in trash_dic:
                    del(trash_dic[key - num])
                    trash_pair += 1
                else:
                    trash_dic[num] = 1
                    
        check += 2
        if pair_num == 0 and coin >= 2 and trash_pair > 0:
            pair_num += 1
            coin -= 2
            trash_pair -= 1

    return (check - n // 3) // 2