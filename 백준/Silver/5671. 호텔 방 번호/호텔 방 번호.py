from collections import Counter

def check(num):
    s_num = str(num)
    for k, v in Counter(s_num).items():
        if v >= 2:
            return 0
    return 1
    
while True:
    try:
        n, m = map(int, input().split())
        answer = 0
        for num in range(n, m + 1):
            if check(num):
                answer += 1
        print(answer)
    except:
        break