from collections import Counter

def solution(food_times, k):
    dic = Counter(food_times)
    sorted_list = sorted(dic)
    
    now_max = len(food_times)
    idx = 0
    before_food = 0
    while True:
        now_food = sorted_list[idx] - before_food
        if now_max * now_food > k:
            k %= now_max
            break
        else:
            k -= now_max * now_food
            before_food = sorted_list[idx]
            now_max -= dic[before_food]
            idx += 1
        if idx == len(sorted_list):
            return -1
    count = -1
    for idx, food in enumerate(food_times):
        if food > before_food:
            count += 1
        if count == k:
            answer = idx + 1
            break
    return answer