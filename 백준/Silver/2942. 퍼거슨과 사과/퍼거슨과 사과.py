def div(a, b):
    while b != 0:
        if a > b:
            a, b = b, a % b
        elif b > a:
            a, b = b, a
        else:
            break
    return a

def find(num):
    answer = []
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            answer.append(i)
            if i ** 2 != num:
                answer.append(num // i)
    return answer
        
r, g = map(int, input().split())

for num in find(div(r, g)):
    print(num, r // num, g // num)