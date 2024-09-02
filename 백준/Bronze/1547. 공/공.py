n = int(input())
dic = {1:1, 2:2, 3:3}
for _ in range(n):
    first, second = map(int, input().split())
    dic[first], dic[second] = dic[second], dic[first]
    
for k, v in dic.items():
    if v == 1:
        print(k)