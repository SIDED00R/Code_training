weight = [13, 7, 5, 3, 3, 2]
choi = list(map(int, input().split()))
han = list(map(int, input().split()))
c_w = 0
h_w = 1.5
for idx in range(6):
    c_w += weight[idx] * choi[idx]
    h_w += weight[idx] * han[idx]
    
if c_w > h_w:
    print('cocjr0208')
else:
    print('ekwoo')
    