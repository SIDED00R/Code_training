answer_dic = {}
prime_list = [0] * 1000000
prime_list[0] = 1
prime_list[1] = 1
for idx in range(2, 1000000):
    if prime_list[idx] == 0:
        answer_dic[idx ** 2] = 1
        for i in range(idx, 1000000, idx):
            prime_list[i] = 1
n = int(input())
line = list(map(int, input().split()))
            
for num in line:
    if num in answer_dic:
        print("YES")
    else:
        print("NO")