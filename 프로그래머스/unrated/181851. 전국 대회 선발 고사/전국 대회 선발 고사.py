def solution(rank, attendance):
    attend = []
    for idx, can in enumerate(attendance):
        if can:
            attend.append(rank[idx])
    attend = sorted(attend)
    return rank.index(attend[0])*10000 + rank.index(attend[1])*100 + rank.index(attend[2])