check_list = [False] * 50001
prime_list = []
for num in range(2, 50001):
    if check_list[num] == False:
        prime_list.append(num)
        for idx in range(num, len(check_list), num):
            check_list[idx] = True

def underprime(answer):
    for num in prime_list:
        next_num = num
        while next_num < len(answer):
            for idx in range(next_num, len(answer), next_num):
                answer[idx] += 1
            next_num *= num
A, B = map(int, input().split())
answer = [0] * (B + 1)
underprime(answer)
ans = 0
for n in range(A, B + 1):
    if answer[n] in prime_list:
        ans += 1
        
print(ans)
