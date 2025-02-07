import sys
input = sys.stdin.readline

def find(l, ln, n):
    answer = 0
    for idx in range(ln // 2):
        front = l[idx] + 1
        back = n - l[-idx - 1]
        answer += abs(front - back)
    return answer

line = list(input().rstrip('\n'))
n = len(line)
a = []
b = []
for idx in range(n):
    if line[idx] == "a":
        a.append(idx)
    else:
        b.append(idx)

an = len(a)
bn = len(b)

if an % 2 == 0:
    print(find(a, an, n))
elif bn % 2 == 0:
    print(find(b, bn, n))
else:
    print(-1)