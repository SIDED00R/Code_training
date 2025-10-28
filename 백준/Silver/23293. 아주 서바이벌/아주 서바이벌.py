from collections import defaultdict
import sys
input = sys.stdin.readline

t, n = map(int, input().split())
bad = []
bad_p = set()
location = defaultdict(lambda: "1")
things = defaultdict(lambda: defaultdict(int))

for _ in range(t):
    line = list(input().split())   
    if line[2] == "C":
        log, player, code, a, b = line
    else:
        log, player, code, a = line

    if code == "M":
        location[player] = a
    elif code == "F":
        if location[player] != a:
            bad.append(log)
        things[player][a] += 1

    elif code == "C":
        if things[player][a] < 1 or things[player][b] < 1:
            bad.append(log)
        things[player][a] = max(0, things[player][a] - 1)
        things[player][b] = max(0, things[player][b] - 1)
    else:
        if location[player] != location[a]:
            bad.append(log)
            bad_p.add(player)
bad = list(map(int, bad))
bad_p = list(map(int, bad_p))
print(len(bad))
if len(bad) != 0:
    print(" ".join(list(map(str, sorted(bad)))))
print(len(bad_p))
if len(bad_p) != 0:
    print(" ".join(list(map(str, sorted(bad_p)))))
    