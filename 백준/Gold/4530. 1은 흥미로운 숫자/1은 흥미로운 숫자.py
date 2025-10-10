def prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def check(num, stack, idx):
    count = 0
    s = str(num)
    if prime(num):
        count += 1

    for div_num in range(1, int(num ** 0.5) + 1):
        if div_num ** 2 == num:
            count += 1
        if div_num ** 3 == num:
            count += 1
        if div_num ** 4 == num:
            count += 1

    d_total = 0
    m_total = 1
    for d in s:
        d_total += int(d)
        m_total *= int(d)
    if num % d_total == 0:
        count += 1
    if m_total!= 0 and num % m_total == 0:
        count += 1

    left_list = stack[:idx] + stack[idx + 1:]
    find7 = False
    find8 = False
    find9 = False
    find10 = False
    find11 = False
    find12 = False
    find13 = False
    for left_num in left_list:
        if not find7 and left_num % num == 0:
            find7 = True
            count += 1
        if not find8 and num % left_num == 0:
            find8 = True
            count += 1
        if not find9 and left_num ** 2 == num:
            find9 = True
            count += 1
        if not find10 and left_num ** 3 == num:
            find10 = True
            count += 1
        if not find11 and left_num ** 4 == num:
            find11 = True
            count += 1
            
        s = str(left_num)
        d_total = 0
        m_total = 1
        for d in s:
            d_total += int(d)
            m_total *= int(d)
        if not find12 and num % d_total == 0:
            find12 = True
            count += 1
        if not find13 and m_total != 0 and num % m_total == 0:
            find13 = True
            count += 1

        if find7 and find8 and find9 and find10 and find11 and find12 and find13:
            break
    return count

t = int(input())
for test_k in range(t):
    n = int(input())
    stack = []
    for _ in range(n):
        x = int(input())
        stack.append(x)
    max_count = 0
    answer = []
    for idx, num in enumerate(stack):
        count = check(num, stack, idx)
        if max_count < count:
            max_count = count
            answer = [num]
        elif max_count == count:
            answer.append(num)

    print(f"DATA SET #{test_k + 1}")
    for num in sorted(answer):
        print(num)