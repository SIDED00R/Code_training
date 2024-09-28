n = int(input())
for _ in range(n):
    cake = list(map(int, input().split()))[1:]
    total = len(cake)
    now = len(cake)
    answer = []
    for i in range(total):
        if cake[total - i - 1] == now:
            now -= 1
            continue
        else:
            idx = cake.index(now)
            if idx != 0:
                answer.append(idx + 1)
                cake = cake[:idx + 1][::-1] + cake[idx + 1:]
            answer.append(total - i)
            cake = cake[:total - i][::-1] + cake[total - i:]
            now -= 1
    print(len(answer), end = " ")
    for num in answer:
        print(num, end = " ")
    print()
