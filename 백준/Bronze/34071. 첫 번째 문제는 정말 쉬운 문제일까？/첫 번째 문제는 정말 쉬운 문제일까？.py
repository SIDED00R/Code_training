n = int(input())
first = int(input())
answer = 0
total_list = []
for _ in range(n - 1):
    num = int(input())
    total_list.append(num)
    
small = 0
large = 0
for num in total_list:
    if first >= num:
        small = 1
    if first <= num:
        large = 1
        
if small == large:
    print('?')
elif small == 1:
    print('hard')
else:
    print('ez')