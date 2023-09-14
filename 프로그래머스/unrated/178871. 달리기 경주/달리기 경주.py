def solution(players, callings):
    dic = {people : idx for idx, people in enumerate(players)}
    for name in callings:
        idx = dic[name]
        dic[name] , dic[players[idx - 1]] = dic[players[idx - 1]], dic[name]
        players[idx], players[idx - 1] = players[idx - 1], players[idx]
        
    return players