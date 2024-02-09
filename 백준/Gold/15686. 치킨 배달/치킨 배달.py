import sys
input = sys.stdin.readline
from itertools import combinations
from math import inf

N, M = map(int, input().rstrip('\n').split())

city = []
chicken_shop = []
houses = []
for i in range(N):
    line = list(map(int, input().rstrip('\n').split()))
    city.append(line)
    for j, num in enumerate(line):
        if num == 2:
            chicken_shop.append((i, j))
        elif num == 1:
            houses.append((i, j))

answer = inf            
for case in combinations(chicken_shop, M):
    total_length = 0
    for house_i, house_j in houses:
        min_length = 10000
        for shop_i, shop_j in case:
            length = abs(house_i - shop_i) + abs(house_j - shop_j)
            if min_length > length:
                min_length = length
        total_length += min_length
    if answer > total_length:
        answer = total_length
        
print(answer)