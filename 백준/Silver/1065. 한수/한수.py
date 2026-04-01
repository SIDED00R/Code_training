a = int(input())
ad = 0
for i in range(1,a+1):
    num_list = list(map(int, str(i)))
    if i < 100:
        ad += 1  
    elif num_list[0]-num_list[1] == num_list[1]-num_list[2]:
        ad += 1  
print(ad)