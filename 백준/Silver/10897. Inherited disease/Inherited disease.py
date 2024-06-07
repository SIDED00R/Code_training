n = int(input())
D = list(map(int, input().split()))
front = 1
line_count = [1]
front = [1]
total_diff = 0
for idx in range(1, n):
    line_count.append(idx * line_count[-1])
    front.append(line_count[-1] + front[-1])
    
for idx in range(n):
    num = D[idx]
    diff = num - 1
    total_diff = total_diff * (idx + 1) + diff
    print((front[idx] + total_diff) % 1000000007)