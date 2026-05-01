import math

n = int(input())
line = list(input().split())
dic = {"1":0, "2":0, "3":0, "4":0}
for count in line:
    dic[count] += 1
answer = dic["4"]
    
answer += dic["3"]
dic["1"] = max(dic["1"] - dic["3"], 0)
    
answer += dic["2"] // 2
if dic["2"] % 2 == 1:
    answer += 1
    dic["1"] = max(dic["1"] - 2, 0)
        
answer += math.ceil(dic["1"] / 4)

print(answer)