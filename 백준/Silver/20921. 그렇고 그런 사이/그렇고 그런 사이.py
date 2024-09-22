n, k = map(int, input().split())
check = 0
num = n - 1
answer = []
all_number = [i for i in range(1, n + 1)]

while all_number:
    if check + num <= k:
        check += num
        now = all_number.pop()
        answer.append(now)
        num -= 1
    else:
        idx = k - check
        answer.append(all_number[idx])
        answer += all_number[:idx] + all_number[idx + 1:]
        break

for num in answer:
    print(num, end = " ")