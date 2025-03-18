n = int(input())
for _ in range(n):
    s = set()
    word = input()
    for idx in range(1, len(word)):
        first = word[:idx]
        last = word[idx:]
        s.add(first + last)
        s.add(first[::-1] + last)
        s.add(first + last[::-1])
        s.add(first[::-1] + last[::-1])
        s.add(last + first)
        s.add(last[::-1] + first)
        s.add(last + first[::-1])
        s.add(last[::-1] + first[::-1])
    print(len(s))