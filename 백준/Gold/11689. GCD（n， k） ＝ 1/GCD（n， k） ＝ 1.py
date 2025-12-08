def find(n):
    answer = []
    for num in range(2, int(n ** 0.5) + 1):
        if n % num == 0:
            answer.append(num)
            while n % num == 0:
                n //= num
    if n != 1:
        answer.append(n)
    return answer
            
n = int(input())

if n == 1:
    print(1)
else:
    answer = n
    for p in find(n):
        answer = answer // p * (p - 1)
    print(answer)