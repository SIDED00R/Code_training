from collections import defaultdict, deque
n = int(input())
A = list(map(int, input().split()))
dic = defaultdict(int)
for num in A:
    dic[num] += 1
    
sorted_A = sorted(A)

stack = deque()

for num in A[::-1]:
    stack.appendleft(sorted_A.index(num) + dic[num] - 1)
    dic[num] -= 1

for i in stack:
    print(i, end = " ")
