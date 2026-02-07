from itertools import combinations

W = [input() for _ in range(4)]

def count_for_assignment(H1, H2, V1, V2):
    ans = 0
    lenH1, lenH2, lenV1, lenV2 = map(len, (H1, H2, V1, V2))

    # H1-V1 교차 (a,i)
    for a in range(lenH1):
        ch_a = H1[a]
        for i in range(lenV1):
            if V1[i] != ch_a:
                continue

            for b in range(a + 2, lenH1):
                ch_b = H1[b]
                dx = b - a
                for j in range(lenV2):
                    if V2[j] != ch_b:
                        continue

                    for k in range(i + 2, lenV1):
                        dy = k - i
                        for c in range(lenH2):
                            if H2[c] != V1[k]:
                                continue

                            d = c + dx
                            l = j + dy
                            if d < lenH2 and l < lenV2 and H2[d] == V2[l]:
                                ans += 1
    return ans

total = 0

for horiz_idx in combinations(range(4), 2):
    vert_idx = [x for x in range(4) if x not in horiz_idx]
    h0, h1 = horiz_idx
    v0, v1 = vert_idx

    total += count_for_assignment(W[h0], W[h1], W[v0], W[v1])
    total += count_for_assignment(W[h1], W[h0], W[v0], W[v1])
    total += count_for_assignment(W[h0], W[h1], W[v1], W[v0])
    total += count_for_assignment(W[h1], W[h0], W[v1], W[v0])

print(total)
