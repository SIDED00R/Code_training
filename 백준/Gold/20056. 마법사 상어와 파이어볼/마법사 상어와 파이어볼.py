from collections import defaultdict

def is_odd(l):
    for num in l:
        if num % 2 == 0:
            return False
    return True
    
def is_even(l):
    for num in l:
        if num % 2 == 1:
            return False
    return True

n, m, k = map(int, input().split())
fire_stack = []
di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]
for _ in range(m):
    fire_stack.append(list(map(int, input().split())))

for _ in range(k):
    dic = defaultdict(list)
    for now_case in fire_stack:
        r, c, weight, s, d = now_case
        nr = (r + di[d] * s) % n
        nc = (c + dj[d] * s) % n
        dic[(nr, nc)].append([weight, s, d])
    for k, v in dic.items():
        if len(v) > 1:
            total_weight = 0
            total_s = 0
            d_list = []
            for now_v in v:
                weight, s, d = now_v
                total_weight += weight
                total_s += s
                d_list.append(d)
            now_weight = int(total_weight / 5)
            if now_weight == 0:
                dic[k] = []
                continue
            else:
                now_s = int(total_s / len(v))
                if is_odd(d_list) or is_even(d_list):
                    dic[k] = [[now_weight, now_s, i] for i in [0, 2, 4, 6]]
                else:
                    dic[k] = [[now_weight, now_s, i] for i in [1, 3, 5, 7]]
    fire_stack = []
    for k, v in dic.items():
        r, c = k
        for now_v in v:
            weight, s, d = now_v
            fire_stack.append([r, c, weight, s, d])
answer = 0
for now_case in fire_stack:
    r, c, weight, s, d = now_case 
    answer += weight

print(answer)