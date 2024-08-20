from itertools import combinations

n = int(input())

dic = {}
able_case = list(combinations(range(5), 2))
for days in able_case:
    dic[days] = 0

for _ in range(n):
    line = list(map(int, input().split()))
    for days in able_case:
        first, second = days
        if line[first] == 1 and line[second] == 1:
            dic[days] += 1

max_value = 0
answer = (0, 1)
for key, value in dic.items():
    if value > max_value:
        answer = key
        max_value = value
        
answer_list = [0 for _ in range(5)]
for d in answer:
    answer_list[d] = 1
    
print(max_value)
for num in answer_list:
    print(num, end = " ")