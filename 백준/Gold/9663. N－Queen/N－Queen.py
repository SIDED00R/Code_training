N = int(input())
count = 0

def queen(q, now_able, N):
    global count
    n = len(q)
    if n == N:
        count += 1
    for i in range(len(now_able)):
        go = True
        next_value = now_able[i]
        for idx, value in enumerate(q):
            length = n - idx
            if abs(next_value - value) == length:
                go = False
                break
        if go:
            next_able = now_able[:i] + now_able[i + 1:]
            q.append(next_value)
            queen(q, next_able, N)
            q.pop()
    return 

able = [num for num in range(N)]
q = []
queen(q, able, N)
print(count)
