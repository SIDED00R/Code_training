n = int(input())
dic = {"00":0, "01":0, "10":0, "11":0}
answer = 0
for _ in range(n):
    line = input()
    dic[line[0] + line[-1]] += 1
    start = line[0]
    for num in line[1:]:
        if num != start:
            start = num
            answer += 1
            
if dic["01"] == 0 and dic["10"] == 0:
    if dic["00"] != 0 and dic["11"] != 0:
        answer += 1
else:
    answer += max(abs(dic["01"] - dic["10"]) - 1, 0)
    
print(answer)