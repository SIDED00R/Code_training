def find(r, l, n):
    addl, addr = 0, 0
    for i in range(2):
        addl += abs(l[i] - n[i])
        addr += abs(r[i] - n[i])
    return "same" if addl == addr else addl > addr
    


def solution(numbers, hand):
    l = [0, 0]
    r = [2, 0]
    answer = ""
    for num in numbers:
        if num in [1, 4, 7]:
            answer += "L"
            l = [0, 3 - num // 3]
        elif num in [3, 6, 9]:
            answer += "R"
            r = [0, 4 - num // 3]
            
        else:
            a = [0, 0, 3, 0, 0, 2, 0, 0, 1]
            n = [1, a[num]]
            if find(r, l, n) == "same":
                if hand == "right":
                    r = n
                    answer += "R"
                else:
                    l = n
                    answer += "L"
            elif find(r, l, n):
                r = n
                answer += "R"
            else:
                l = n
                answer += "L"
            
    return answer