from collections import defaultdict

u, n = map(int, input().split())
dic = defaultdict(int)
value = [[] for _ in range(u + 1)]
for _ in range(n):
    name, num = input().split()
    num = int(num)
    dic[num] += 1
    value[num].append(name)
    
min_count = n + 1
min_value = u + 1
for key, values in dic.items():
    if values < min_count:
        min_count = values
        min_value = key
    elif values == min_count and key < min_value:
        min_count = values
        min_value = key
        
print(value[min_value][0], min_value)