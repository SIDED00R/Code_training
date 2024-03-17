import sys
input = sys.stdin.readline

def find_solution(first_liquid, second_liquid, now_idx, state, answer):
    keep = first_liquid[now_idx]
    first_liquid_change = first_liquid[:now_idx] + first_liquid[now_idx + 1:]

    if not first_liquid_change:
        return answer
    else:
        first_liquid_idx = 0
        
    if not second_liquid:
        return answer
    else:
        second_liquid_idx = 0
    
    first = first_liquid_change[first_liquid_idx]
    second = second_liquid[second_liquid_idx]
    while True:
        mix = first + second + keep
        
        if abs(mix) < answer[0]:
            answer = [abs(mix), first, second, keep]
        if mix > 0:
            try:
                if state == "acid":
                    first_liquid_idx += 1
                    first = first_liquid_change[first_liquid_idx]
                else:
                    second_liquid_idx += 1
                    second = second_liquid[second_liquid_idx]
            except:
                return answer
        elif mix < 0:
            try:
                if state == "acid":
                    second_liquid_idx += 1
                    second = second_liquid[second_liquid_idx]
                else:
                    first_liquid_idx += 1
                    first = first_liquid_change[first_liquid_idx]
            except:
                return answer
        else:
            return answer



n = int(input())
line = list(map(int, input().rstrip('\n').split()))
line = sorted(line)

change_idx = n
for idx, num in enumerate(line):
    if num > 0:
        change_idx = idx
        break
    
base = line[change_idx:]
acid = line[:change_idx][::-1]

answer = [3000000001, 0, 0, 0]
if len(acid) > 2 and answer[0] > abs(sum(acid[:3])):
    answer = [abs(sum(acid[:3])), acid[0], acid[1], acid[2]]
if len(base) > 2 and answer[0] > abs(sum(base[:3])):
    answer = [abs(sum(base[:3])), base[2], base[1], base[0]]

for idx in range(len(acid)):
    answer = find_solution(acid, base, idx, "acid", answer)

for idx in range(len(base)):
    answer = find_solution(base, acid, idx, "base", answer)

solution = answer[1:]
solution.sort()
for num in solution:
    print(num, end = " ")