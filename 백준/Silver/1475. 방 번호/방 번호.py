from collections import defaultdict

dic = defaultdict(int)
for num in list(input()):
    dic[num] += 1
    
max_count = 0
for key, value in dic.items():
    if key not in ['6', '9']:
        if value > max_count:
            max_count = value
            
special_case = (dic['6'] + dic['9'] + 1) // 2
print(max(max_count, special_case))