t = int(input())
for _ in range(t):
    first = input()
    second = input()
    f_length = len(first)
    s_length = len(second)
    w = input()
    
    ffront = [-1 for _ in range(len(w) + 1)]
    fback = [f_length for _ in range(len(w) + 1)]
    sfront = [-1 for _ in range(len(w) + 1)]
    sback = [s_length for _ in range(len(w) + 1)]

    for idx in range(len(w)):
        for f_idx in range(ffront[idx] + 1, f_length):
            if first[f_idx] == w[idx]:
                ffront[idx + 1] = f_idx
                break
        for s_idx in range(sfront[idx] + 1, s_length):
            if second[s_idx] == w[idx]:
                sfront[idx + 1] = s_idx
                break
    for idx in range(len(w) - 1, -1, -1):
        for f_idx in range(fback[idx + 1] - 1, -1, -1):
            if w[idx] == first[f_idx]:
                fback[idx] = f_idx
                break
        for s_idx in range(sback[idx + 1] - 1, -1, -1):
            if w[idx] == second[s_idx]:
                sback[idx] = s_idx
                break
    find = False
    for w_idx in range(len(w) + 1):
        f_front_end = ffront[w_idx]
        f_back_start = fback[w_idx]
        f_set = set(first[f_front_end + 1:f_back_start])
        s_front_end = sfront[w_idx]
        s_back_start = sback[w_idx]
        s_set = set(second[s_front_end + 1:s_back_start])
        if f_set & s_set:
            find = True
            break
    if find:
        print(1)
    else:
        print(0)