import math

def check(num_list):
    for idx in range(1, len(num_list)):
        if num_list[idx] < num_list[idx - 1]:
            return False
    return True

def r_comb(n, r):
    answer = 1
    c = n + r - 1
    for _ in range(r):
        answer *= c
        c -= 1
    return answer // math.factorial(r)

def find(num_list):
    answer = 0
    for n in range(num_list[0]):
        answer += r_comb(10 - n, len(num_list) - 1)
    for idx in range(1, len(num_list)):
        for n in range(num_list[idx - 1], num_list[idx]):
            answer += r_comb(10 - n, len(num_list) - idx - 1)
    return answer

n = int(input())
for _ in range(n):
    number = list(map(int, list(input())))
    if check(number):
        print(find(number))
    else:
        print(-1)