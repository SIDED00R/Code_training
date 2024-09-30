n, m, k = map(int, input().split())
heros = list(map(int, input().split()))
monster_levels = list(map(int, input().split()))
sort_level = sorted(monster_levels)

def find_level(num):
    s = 0
    e = len(sort_level) - 1
    while s <= e:
        mid = (s + e) // 2
        if sort_level[mid] > num:
            e = mid -1
        else:
            s = mid +1
    if s == 0:
        return sort_level[0]
    else:
        return sort_level[s -1]

dic = {monster_levels[idx]: idx + 1 for idx in range(len(monster_levels))}

levels = [0] * 201 
for hero in heros:
    levels[hero] += 1
    end_level = min(hero + k, 200)
    levels[end_level] -= 1

for idx in range(1, 201):  
    levels[idx] += levels[idx -1]

y = 2
total_time = 0
for level in range(1, 201):
    people_num = levels[level]
    if people_num == 0:
        continue
    total_time += (dic[find_level(level)] -1) * people_num

min_time = total_time
for i in range(2, m+1):
    now_time = 0
    for level in range(1, 201):
        people_num = levels[level]
        if people_num == 0:
            continue
        else:
            if dic[find_level(level)] ==1:
                continue
            now_time += people_num * min(abs(dic[find_level(level)] - i), dic[find_level(level)] -1)
    if now_time < min_time:
        y = i
        min_time = now_time

print(1, y)
print(total_time - min_time)
