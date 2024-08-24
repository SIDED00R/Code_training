import sys

def check(a_list, b_list):
    for i in range(n):
        start, end = a_list[i]
        if start == -1 and end == -1:
            continue
        elif start == -1 or end == -1 or start > end:
            print("NE")
            exit()
        else:
            s_s, s_e = b_list[start]
            if s_s == -1 or s_e == -1:
                print("NE")
                exit()
            elif s_s <= i <= s_e:
                continue
            else:
                print("NE")
                exit()
            
            e_s, e_e = b_list[end]
            if e_s == -1 or e_e == -1:
                print("NE")
                exit()
            elif e_s <= i <= e_e:
                continue
            else:
                print("NE")
                exit()
            
            for idx in range(start + 1, end):
                s, e = b_list[idx]
                if s == -1 or e == -1:
                    print("NE")
                    exit()
                elif s == i or i == e:
                    continue
                else:
                    print("NE")
                    exit()

n = int(input())
r_l_list = [[] for _ in range(n)]
u_d_list = [[] for _ in range(n)]

for idx in range(4):
    line = list(map(int, sys.stdin.readline().rstrip('\n').split()))
    for i, num in enumerate(line):
        if idx == 0:
            if line[i] == -1:
                r_l_list[i].append(-1)
            else:
                r_l_list[i].append(num)
        
        elif idx == 1:
            if line[i] == -1:
                r_l_list[i].append(-1)
            else:
                r_l_list[i].append(n - num - 1)
                
        elif idx == 2:
            if line[i] == -1:
                u_d_list[i].append(-1)
            else:
                u_d_list[i].append(num)
        
        elif idx == 3:
            if line[i] == -1:
                u_d_list[i].append(-1)
            else:
                u_d_list[i].append(n - num - 1)
                

            
check(r_l_list, u_d_list)
check(u_d_list, r_l_list)
print("DA")