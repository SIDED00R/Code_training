from collections import defaultdict

n = int(input())
A = []
B = []
C = []
D = []
for _ in range(n):
    line = list(map(int, input().split()))
    A.append(line[0])
    B.append(line[1])    
    C.append(line[2])
    D.append(line[3])  
 
ab_dic = defaultdict(int)
for num_a in A:
    for num_b in B:
        ab_dic[num_a + num_b] += 1
        
answer = 0
for num_c in C:
    for num_d in D:
        if -(num_c + num_d) in ab_dic:
            answer += ab_dic[-(num_c + num_d)]
        
print(answer)
        