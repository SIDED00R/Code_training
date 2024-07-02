from collections import defaultdict

dic = defaultdict(int)
n = int(input())
line = list(map(int, input().split()))
for num in line:
    dic[num] += 1
    
double = True
max_count = 0

for key, value in dic.items():
    if key != 0:
        if value > max_count:
            max_count = value
            answer = key
            double = False
        elif value == max_count:
            double = True
            
if double:
    print("skipped")
else:
    print(answer)