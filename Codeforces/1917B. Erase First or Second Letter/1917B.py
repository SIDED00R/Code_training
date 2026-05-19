t = int(input())

for _ in range(t):
    n = int(input())
    word = input()

    used = set()
    answer = 0

    for ch in word:
        used.add(ch)
        answer += len(used)

    print(answer)