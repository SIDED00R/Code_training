def compair(a, b):
    long_len = len(a)
    short_len = len(b)
    answer = short_len + long_len
    for idx in range(1, short_len):
        find = True
        for i in range(idx):
            if b[-i - 1] + a[idx - i - 1] == 4:
                find = False
                break
        if find:    
            answer = min(answer, long_len + short_len - idx)

        find = True
        for i in range(idx):
            if b[idx - i - 1] + a[-i - 1] == 4:
                find = False
                break
        if find:    
            answer = min(answer, long_len + short_len - idx)

    for idx in range(long_len - short_len + 1):
        find = True
        for i in range(short_len):
            if b[i] + a[idx + i] == 4:
                find = False
                break
        if find:    
            answer = long_len
            return answer

    return answer


first = list(map(int, list(input())))
second = list(map(int, list(input())))

if len(first) > len(second):
    print(compair(first, second))
else:
    print(compair(second, first))