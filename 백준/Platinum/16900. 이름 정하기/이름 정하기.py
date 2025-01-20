import sys

def KMP_table(pattern):
    lp = len(pattern)
    tb = [0 for _ in range(lp)]
    
    pidx = 0
    for idx in range(1, lp):
        while pidx > 0 and pattern[pidx] != pattern[idx]:
            pidx = tb[pidx-1]
        
        if pattern[idx] == pattern[pidx] :
            pidx += 1
            tb[idx] = pidx
    
    return tb

input = sys.stdin.readline
name, num = input().split()
num = int(num)

count = KMP_table(name)[-1]

print((num - 1) * (len(name) - count) + len(name))