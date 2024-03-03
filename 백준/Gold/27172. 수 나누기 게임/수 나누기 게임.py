import sys
input = sys.stdin.readline

n = int(input())
line = list(map(int, input().rstrip('\n').split()))
line_set = set(line)
answer = [0] * 1000001

for num in line:
    for mul_num in range(num * 2, 1000001, num):
        if mul_num in line_set:
            answer[num] += 1
            answer[mul_num] -= 1
            
for num in line:
    print(answer[num], end = " ")