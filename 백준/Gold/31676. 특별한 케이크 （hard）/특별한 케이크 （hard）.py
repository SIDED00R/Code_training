import sys
from collections import defaultdict

input = sys.stdin.read
data = input().splitlines()

# 첫 번째 줄 무시 (swi's cake is missing!)
n = int(data[1])

cnt = defaultdict(int)
lb = 0

for i in range(1, n + 1):
    m = int(data[3 * (i - 1) + 2])  # 명단에 포함된 학생 수
    tmp = list(map(int, data[3 * (i - 1) + 3].split()))  # 명단
    b = int(data[3 * (i - 1) + 4])  # 진술 유형

    if b:  # 명단에 범인이 있다
        for s in tmp:
            cnt[s] += 1
            if s == i:  # 자기 자신을 범인으로 지목하지 않는 경우
                cnt[s] = -1234567
    else:  # 명단에 범인이 없다
        lb -= 1
        flag = True
        for s in tmp:
            cnt[s] -= 1
            if s == i:
                flag = False
        if flag:  # 명단에 자기 자신이 포함되지 않는 경우
            cnt[i] = -1234567

ans = []

# 범인일 가능성이 있는 학생들을 찾기
for i in range(1, n + 1):
    if cnt[i] - lb == n - 1:
        ans.append(i)

# 결과 출력
if not ans:
    print("swi")
else:
    print(" ".join(map(str, ans)))
