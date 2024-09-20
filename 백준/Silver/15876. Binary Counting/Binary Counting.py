n, k = map(int, input().split())
answer = []
now_num = 1
total = "0"
while len(answer) != 5:
    total += bin(now_num).lstrip("0b")
    if len(total) >= n:
        answer.append(total[k - 1])
        total = total[n:]
    now_num += 1

for num in answer:
    print(num, end = " ")