import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def find(num_map, now, N, M):
    now_i, now_j = now
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]
    count = 1
    for i in range(4):
        next_i = now_i + di[i]
        next_j = now_j + dj[i]
        if 0 <= next_i < N and 0 <= next_j < M and num_map[next_i][next_j] == "0":
            num_map[next_i][next_j] = "-1"
            count += find(num_map, [next_i, next_j], N, M)
    return count
        
def fill(num_map, now, N, M, count, group):
    now_i, now_j = now
    num_map[now_i][now_j] = [count, group]
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]
    for i in range(4):
        next_i = now_i + di[i]
        next_j = now_j + dj[i]
        if 0 <= next_i < N and 0 <= next_j < M and num_map[next_i][next_j] == "-1":
            fill(num_map, [next_i, next_j], N, M, count, group)
    return

N, M = map(int, input().split())
num_map = []
for _ in range(N):
    line = list(input().rstrip('\n'))
    num_map.append(line)
    
group = 1
for i in range(N):
    for j in range(M):
        if num_map[i][j] == "0":
            group += 1
            num_map[i][j] = "-1"
            count = find(num_map, [i, j], N, M)
            fill(num_map, [i, j], N, M, count + 1, group)

answer = [[0 for _ in range(M)] for _ in range(N)]
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
for i in range(N):
    for j in range(M):
        if num_map[i][j] != "1":
            answer[i][j] = 0
        else:
            total = 1
            case = []
            for idx in range(4):
                next_i = i + di[idx]
                next_j = j + dj[idx]
                if 0 <= next_i < N and 0 <= next_j < M and num_map[next_i][next_j] != "1": 
                    case.append(num_map[next_i][next_j])
            for case_idx in range(len(case)):
                able = True
                for back_idx in range(case_idx + 1, len(case)):
                    if case[case_idx][1] == case[back_idx][1]:
                        able = False
                if able:
                    total += case[case_idx][0] - 1
            answer[i][j] = total % 10
            
for line in answer:
    print("".join(map(str, line)))