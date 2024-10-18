import sys

def find_min_max(letter, word):
    length = len(word)
    front = back = -1
    for idx in range(length):
        if word[idx] == letter:
            front = idx + 1
            break
    for idx in range(1, length + 1):
        if word[-idx] == letter:
            back = length - idx + 1
            break
    return front ,back


t = int(input())
for _ in range(t):
    n = int(input())
    word = sys.stdin.readline().rstrip('\n')

    if n in [1, 3]:
        print(-1)
    elif n == 2:
        if word[0] == word[1]:
            print(1)
        else:
            print(0)
    else:
        if word[0] == word[-1]:
            if word[1] == word[-2]:
                print(2)
            else:
                print(1)
        else:
            ff, fb = find_min_max(word[0], word)
            sf, sb = find_min_max(word[-1], word)
            if (fb - ff) == (sb - sf):
                print(0)
            else:
                if n % 2 == 0:
                    print(1)
                else:
                    if (fb == (n + 1) // 2 and fb + 1 == sf) or (sf == (n + 1) // 2 and fb + 1 == sf):
                        print(2)
                    else:
                        print(1)
