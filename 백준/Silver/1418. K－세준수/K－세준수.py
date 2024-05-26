N = int(input())
K = int(input())
num_list = [0] * (N + 1)
for idx in range(2, N + 1):
    if num_list[idx] == 0:
        for i in range(idx, N + 1, idx):
            if idx > K:
                num_list[i] = -1
            else:
                num_list[i] = 1
            
print(N - (N - sum(num_list)) // 2)