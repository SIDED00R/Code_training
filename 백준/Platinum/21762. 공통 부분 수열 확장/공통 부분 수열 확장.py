import sys
from array import array

input = sys.stdin.readline
ALPHA = 26

def build_next(s: str):
    n = len(s)
    sb = s.encode()
    nextpos = []
    for c in range(ALPHA):
        arr = array('I', [n]) * (n + 1)
        last = n
        for i in range(n - 1, -1, -1):
            if sb[i] - 97 == c:
                last = i
            arr[i] = last
        nextpos.append(arr)
    return nextpos

def build_prev(s: str):
    n = len(s)
    sb = s.encode()
    prevpos = []
    for c in range(ALPHA):
        arr = array('i', [-1]) * (n + 1)  # i는 "경계" 0..n
        last = -1
        for i in range(n):
            if sb[i] - 97 == c:
                last = i
            arr[i + 1] = last
        prevpos.append(arr)
    return prevpos

t = int(input())

for _ in range(t):
    first = input().strip()
    second = input().strip()
    w = input().strip()

    n, m, k = len(first), len(second), len(w)

    nextF = build_next(first)
    prevF = build_prev(first)
    nextS = build_next(second)
    prevS = build_prev(second)

    # ffront[i] = first에서 w[0:i]를 매칭한 뒤 다음 시작 위치(= 마지막매칭+1)
    ffront = [0] * (k + 1)
    sfront = [0] * (k + 1)

    for i in range(k):
        c = ord(w[i]) - 97
        p = nextF[c][ffront[i]]
        q = nextS[c][sfront[i]]
        # w는 공통부분수열이므로 p!=n, q!=m 보장
        ffront[i + 1] = p + 1
        sfront[i + 1] = q + 1

    # fback[i] = first에서 w[i:]를 매칭할 때 w[i]가 놓일 수 있는 위치(인덱스)
    fback = [0] * (k + 1)
    sback = [0] * (k + 1)
    fback[k] = n
    sback[k] = m

    posF = n
    posS = m
    for i in range(k - 1, -1, -1):
        c = ord(w[i]) - 97
        posF = prevF[c][posF]  # posF 미만에서 마지막 c
        posS = prevS[c][posS]
        fback[i] = posF
        sback[i] = posS

    find = False
    for i in range(k + 1):
        lF = ffront[i]
        rF = fback[i] if i < k else n
        lS = sfront[i]
        rS = sback[i] if i < k else m

        if lF >= rF or lS >= rS:
            continue

        # 26개 문자만 검사
        for c in range(ALPHA):
            if nextF[c][lF] < rF and nextS[c][lS] < rS:
                find = True
                break
        if find:
            break

    print(1 if find else 0)
