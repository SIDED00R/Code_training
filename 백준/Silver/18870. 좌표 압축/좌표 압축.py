import sys

input = sys.stdin.readline
N = int(input())
numbers = list(map(int, input().split()))
sorted_numbers = sorted(numbers)
dic = {}
idx = 0
now = 0.1
for num in sorted_numbers:
    if now != num:
        now = num
        dic[num] = idx
        idx += 1

answer = []
for number in numbers:
    answer.append(str(dic[number]))

print(" ".join(answer))
