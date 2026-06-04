from collections import Counter
import math
first = Counter(input())
second = Counter(input())

if "+" not in first:
    first["+"] = 0
if "-" not in first:
    first["-"] = 0
if "+" not in second:
    second["+"] = 0
if "-" not in second:
    second["-"] = 0
if "?" not in second:
    second["?"] = 0
    
goal = first["+"] - first["-"]
now = second["+"] - second["-"]
left = second["?"]
diff = abs(goal - now)
if diff > left or (left - diff) % 2 == 1:
    print(0)
else:
    add = (left - diff) // 2
    print(math.comb(left, add) / (2 ** left))