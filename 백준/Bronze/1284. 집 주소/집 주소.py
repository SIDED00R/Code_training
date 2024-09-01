dic = {'0':4, '1': 2}
while True:
    n = list(input())
    if n == ['0']:
        break
    answer = 0
    for num in n:
        if num in dic:
            answer += dic[num]
        else:
            answer += 3
    print(answer + len(n) + 1)