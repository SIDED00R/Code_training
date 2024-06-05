n = int(input())
dic = {}
dic["ChongChong"] = 1
for _ in range(n):
    first, second = input().split()
    if first not in dic:
       dic[first] = 0
    if second not in dic:
        dic[second] = 0
    if dic[first] == 1 or dic[second] == 1:
        dic[first] = 1
        dic[second] = 1   
count = 0
for key, value in dic.items():
    if value == 1:
        count += 1
        
print(count)