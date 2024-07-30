n = int(input())
computer = []
for i in range(n):
    tier, t = map(int, input().split())
    computer.append([tier, t, i + 1])
    
computer = sorted(computer, reverse=True)

now_tier = 1
stack = []
before_stack = []
while computer:
    if computer[-1][0] == now_tier:
        stack.append(computer.pop())
    else:
        if before_stack:
            keep = []
            for case in stack:
                tier, t, idx = case
                maximum_time = 0
                for before_case in before_stack:
                    before_t, before_idx = before_case
                    maximum_time = max(maximum_time, before_t + (before_idx - idx) ** 2 + t)
                keep.append([maximum_time, idx])
            before_stack = keep[:]
        else:
            for case in stack:
                tier, t, idx = case
                before_stack.append([t, idx])
        now_tier += 1
        stack = []
    
maximum_time = 0
for case in stack:
    tier, t, idx = case
    for before_case in before_stack:
        before_t, before_idx = before_case
        maximum_time = max(maximum_time, before_t + (before_idx - idx) ** 2 + t)
print(maximum_time)   