import sys
input = sys.stdin.readline

n = int(input())
line = list(map(int, input().rstrip('\n').split()))
line.sort()

change_idx = n
for idx, num in enumerate(line):
    if num > 0:
        change_idx = idx
        break
    
acid = line[change_idx:]
base = line[:change_idx][::-1]

answer = [2000000001, 0, 0]
if len(acid) > 1 and answer[0] > abs(sum(acid[:2])):
    answer = [abs(sum(acid[:2])), acid[0], acid[1]]
if len(base) > 1 and answer[0] > abs(sum(base[:2])):
    answer = [abs(sum(base[:2])), base[1], base[0]]

try:
    now_acid = acid.pop()
except:
    now_acid = 3000000001
try:
    now_base = base.pop()
except:
    now_base = 3000000001
    
while True:
    mix = now_acid + now_base
    if abs(mix) < answer[0]:
        answer = [abs(mix), now_base, now_acid]
    if mix > 0:
        try:
            now_acid = acid.pop()
        except:
            break
    elif mix < 0:
        try:
            now_base = base.pop()
        except:
            break
    else:
        break

for num in answer[1:]:
    print(num, end = " ")