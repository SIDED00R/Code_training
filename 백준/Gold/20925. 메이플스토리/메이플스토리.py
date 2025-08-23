import sys
from bisect import bisect_right
input = sys.stdin.readline

n, t = map(int, input().split())

C = [0]*n
E = [0]*n
for i in range(n):
    c, e = map(int, input().split())
    C[i] = c
    E[i] = e

matrix = [list(map(int, input().split())) for _ in range(n)]

# 노드를 요구치 C 기준으로 정렬해두고, 에너지 en에 대해 가능한 노드만 빠르게 순회
idx_sorted = sorted(range(n), key=lambda i: C[i])
C_sorted = [C[i] for i in idx_sorted]
min_c = C_sorted[0]

# dp[time][node] = 해당 시각에 그 노드에서 보유한 최대 에너지 (도달 못하면 -1)
dp = [[-1]*n for _ in range(t+1)]
# 원 코드가 dp를 0으로 시작했으므로 동일하게 모든 노드에서 0으로 시작
for i in range(n):
    dp[0][i] = 0

# 활성 상태: 해당 시각에 갱신된 노드만 전개
active = [set() for _ in range(t+1)]
active[0] = set(range(n))

for cur_t in range(t):
    if not active[cur_t]:
        continue
    nxt_set = active[cur_t + 1] if cur_t + 1 <= t else None

    for now in list(active[cur_t]):
        en = dp[cur_t][now]
        if en < 0:
            continue

        # 1) 현재 스테이지 클리어 (시간 +1, 에너지 +E[now])
        if cur_t + 1 <= t and C[now] <= en:
            new_en = en + E[now]
            if dp[cur_t + 1][now] < new_en:
                dp[cur_t + 1][now] = new_en
                nxt_set.add(now)

        # 2) 이동 (시간 + matrix[now][next], 에너지 변화 없음)
        if en >= min_c:
            # c <= en 인 노드까지만 순회
            k = bisect_right(C_sorted, en)  # [0, k) 인덱스들만 가능
            for pos in range(k):
                nxt = idx_sorted[pos]
                travel = matrix[now][nxt]
                if travel <= 0:  # 0 이하 이동시간이면 비정상/무한루프 방지
                    continue
                nt = cur_t + travel
                if nt > t:
                    continue
                if dp[nt][nxt] < en:
                    dp[nt][nxt] = en
                    active[nt].add(nxt)

print(max(dp[t]))
