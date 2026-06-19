import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    letter = input().rstrip('\n')
    if "p" in letter and "s" in letter:
        if letter[0] == "s" and "s" not in letter[1:] or letter[-1] == "p" and "p" not in letter[:-1]:
            print("YES")
        else:
            print("NO")
    else:
        print("YES")