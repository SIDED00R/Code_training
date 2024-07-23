import sys

def search(start, end, num):
    while start <= end:
        mid = (start + end) // 2
        if num < sorted_line[mid]:
            end = mid - 1
        elif num > sorted_line[mid]:
            start = mid + 1
        else:
            return num
    return sorted_line[start]

n = int(input())
line = list(map(int, sys.stdin.readline().split()))
m = int(input())
sorted_line = sorted(line)

count = len(set(line))

if m <= n:
    print(line[m - 1])
else:
    if sorted_line[-1] < count:
        print(count + m - n - 1)
    else:
        try:
            bound = search(0, n - 1, count)
            if count + m - n - 1 <= bound:
                print(count + m - n - 1)
            else:
                print(bound)
        except:
            print(count + m - n - 1)