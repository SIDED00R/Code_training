max_range = int(10000000 ** 0.5) + 1
test_list = [True for _ in range(5000001)]
for idx in range(2, max_range):
    if test_list[idx] == True:
        for i in range(idx * idx, 5000001, idx):
            test_list[i] = False

p_list = []
for idx in range(2, 5000001):
    if test_list[idx]:
        p_list.append(idx)

def count(p, num):
    c = 0
    n = num
    while n:
        n //= p
        c += n
    if c % 2 == 1:
        return c - 1
    else:
        return c
        
while True:
    num = int(input())
    answer = 1
    if num == 0:
        break
    for p in p_list:
        if p * 2 > num:
            break
        now_count = count(p, num)
        now_count = now_count % 1000000006
        answer = (answer * pow(p, now_count, 1000000007) % 1000000007)
    print(answer)
    