from collections import defaultdict
n = int(input())
dic = defaultdict(int)
for _ in range(n):
    a, b = map(int, input().split())
    now_num = a + b
    dic[now_num] += 1
    
answer = 0
for k, v in dic.items():
    answer += 1
print(answer)