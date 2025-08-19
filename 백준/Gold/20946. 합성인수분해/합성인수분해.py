n = int(input())

prime_list = []
for i in range(2, int(n ** 0.5) + 1):
    while n % i == 0:
        prime_list.append(i)
        n //= i
    if n == 1:
        break
if n != 1:
    prime_list.append(n)

length = len(prime_list)
if length == 1:
    print(-1)
elif length % 2 == 0:
    for idx in range(length // 2):
        print(prime_list[idx * 2] * prime_list[idx * 2 + 1], end = ' ')
else:
    for idx in range((length // 2) - 1):
        print(prime_list[idx * 2] * prime_list[idx * 2 + 1], end = ' ')
    print(prime_list[-1] * prime_list[-2] * prime_list[-3])