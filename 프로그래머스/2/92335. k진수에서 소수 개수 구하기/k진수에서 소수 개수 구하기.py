def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    k_num = []
    while n != 0:
        k_num.append(str(n % k))
        n //= k
    able = "".join(k_num[::-1]).split("0")
    for num in able:
        if num == "1" or num == "":
            continue
        else:
            if is_prime(int(num)):
                answer += 1
    return answer