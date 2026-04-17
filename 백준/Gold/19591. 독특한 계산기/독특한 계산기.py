from collections import deque
import sys

input = sys.stdin.readline

def calc(a, op, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        sign = -1 if (a < 0) ^ (b < 0) else 1
        return sign * (abs(a) // abs(b))

line = input().strip()

nums = deque()
ops = deque()

i = 0
n = len(line)

if line[0] == '-':
    j = 1
    while j < n and line[j].isdigit():
        j += 1
    nums.append(int(line[:j]))
    i = j
else:
    j = 0
    while j < n and line[j].isdigit():
        j += 1
    nums.append(int(line[:j]))
    i = j

while i < n:
    ops.append(line[i])
    i += 1
    j = i
    while j < n and line[j].isdigit():
        j += 1
    nums.append(int(line[i:j]))
    i = j

if not ops:
    print(nums[0])
    sys.exit()

priority = {'+': 0, '-': 0, '*': 1, '/': 1}

while ops:
    if len(ops) == 1:
        print(calc(nums[0], ops[0], nums[1]))
        break

    left_op = ops[0]
    right_op = ops[-1]

    if priority[left_op] > priority[right_op]:
        a = nums.popleft()
        b = nums.popleft()
        ops.popleft()
        nums.appendleft(calc(a, left_op, b))

    elif priority[left_op] < priority[right_op]:
        b = nums.pop()
        a = nums.pop()
        ops.pop()
        nums.append(calc(a, right_op, b))

    else:
        left_val = calc(nums[0], left_op, nums[1])
        right_val = calc(nums[-2], right_op, nums[-1])

        if left_val >= right_val:
            a = nums.popleft()
            b = nums.popleft()
            ops.popleft()
            nums.appendleft(left_val)
        else:
            b = nums.pop()
            a = nums.pop()
            ops.pop()
            nums.append(right_val)