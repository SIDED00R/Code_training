t = int(input())
for _ in range(t):
    length = int(input())
    cases = sorted(list(map(int, input().split())))
    answer = sum(cases)
    while True:
        if answer - cases[-1] <= cases[-1]:
            out = cases.pop()
            length -= 1
            answer -= out
        else:
            break
        if length <= 2:
            answer = 0
            break
    print(answer)
    
   