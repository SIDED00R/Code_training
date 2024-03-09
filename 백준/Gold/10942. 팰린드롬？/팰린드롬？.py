import sys
input = sys.stdin.readline

def check(table, idx, line):
    # case1 -> odd
    count = 0
    while count <= idx < len(line) - count and line[idx - count] == line[idx + count]:
        table[idx - count][idx + count] = 1
        count += 1
    
    # case2 -> even
    count = 0
    while count <= idx < len(line) - count - 1 and line[idx - count] == line[idx + 1 + count]:
        table[idx - count][idx + 1 + count] = 1
        count += 1

N = int(input())
line = list(map(int, input().rstrip('\n').split()))

total_table = [[0 for _ in range(N)] for _ in range(N)]
for idx in range(N):
    check(total_table, idx, line)

M = int(input())
for _ in range(M):
    start, end = map(int, input().rstrip('\n').split())
    print(total_table[start - 1][end - 1])