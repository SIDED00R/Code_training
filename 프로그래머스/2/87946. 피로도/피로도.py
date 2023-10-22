from itertools import permutations

def solution(k, dungeons):
    answer = 0
    arr = permutations(dungeons, len(dungeons))
    for case in arr:
        tired = k
        total = 0
        for dungeon in case:
            if dungeon[0] <= tired:
                tired -= dungeon[1]
                total += 1
            else:
                break
        if total > answer:
            
            answer = total

    return answer