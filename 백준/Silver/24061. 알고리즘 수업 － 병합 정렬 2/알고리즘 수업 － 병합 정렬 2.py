import sys

check_count = 0

def merge_sort(p, r, count):
    if p < r:
        q = (p + r) // 2
        merge_sort(p, q, count)      
        merge_sort(q + 1, r, count)  
        merge(p, q, r, count)        

def merge(p, q, r, count):
    global check_count
    tmp = []
    i, j = p, q + 1
    while i <= q and j <= r:
        if line[i] <= line[j]:
            tmp.append(line[i])
            i += 1
        else:
            tmp.append(line[j])
            j += 1
    
    while i <= q:
        tmp.append(line[i])
        i += 1

    while j <= r:
        tmp.append(line[j])
        j += 1

    for k in range(len(tmp)):
        line[p + k] = tmp[k]
        check_count += 1
        if check_count == count:
            for num in line:
                print(num, end = " ")
            exit()

n, k = map(int, input().split())
line = list(map(int, sys.stdin.readline().split()))
merge_sort(0, len(line) - 1, k)

if check_count < k:
    print(-1)