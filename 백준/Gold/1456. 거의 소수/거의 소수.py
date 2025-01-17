def prime():
    p = []
    for idx in range(10 ** 7 + 1):
        if l[idx] == True:
            p.append(idx)
            for i in range(idx, 10 ** 7 + 1, idx):
                l[i] = False
    return p

def find(num):
    ans = []
    for now_num in p:
        if now_num ** 2 > num:
            break
        able = now_num
        while True:
            able *= now_num
            if able <= num:
                ans.append(able)
            else:
                break
    return len(ans)


l = [True for _ in range(10 ** 7 + 1)]
l[0] = False
l[1] = False
p = prime()

a, b = map(int, input().split())
print(find(b) - find(a - 1))