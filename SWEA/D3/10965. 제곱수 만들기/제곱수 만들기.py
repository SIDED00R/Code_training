T = int(input())

prime = [2]
large_num = int(10e7 ** 0.5) + 1
prime_able = [True] * (large_num)
for idx in range(3, large_num, 2):
    if prime_able[idx]:
        prime.append(idx)
        for i in range(idx, large_num, idx):
            prime_able[i] = False  

answer = []
for test_case in range(1, T + 1):
    num = int(input())
    ans = 1
    for p in prime:
        count = 0
        while num % p == 0:
            count += 1
            num //= p
        if count % 2 == 1:
            ans *= p
        if num == 1:
            break
    if num != 1:
        ans *= num
    answer.append(ans)
for answer_idx, a in enumerate(answer):
    print(f"#{answer_idx + 1} {a}")