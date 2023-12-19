def solution(bandage, health, attacks):
    max_health = health
    take_time, heal, more_heal = bandage
    total_time = attacks[-1][0]
    now_attack = 0
    stack = 0
    for i in range(total_time):
        now_time = attacks[now_attack][0]
        if i + 1 == now_time:
            health -= attacks[now_attack][1]
            now_attack += 1
            stack = 0
        else:
            stack += 1
            health += heal
            
        if health <= 0:
            return -1
        if stack == take_time:
            health += more_heal
            stack = 0
        health = min(max_health, health)
            
    return health