from collections import defaultdict

N = int(input())
line = list(map(int, input().split()))
dic = defaultdict(int)

for num in line:
    dic[num] += 1
    
answer = 0

for key, value in dic.items():
    if key == value and answer < key:
        answer = key
        
if answer == 0 and 0 in dic:
    answer = -1
    
print(answer)
    