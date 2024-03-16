import sys
input = sys.stdin.readline

line = list(map(int, input().rstrip('\n').split()))[:-1]
move_weight = {0 : {1 : 2, 2 : 2, 3 : 2, 4 : 2}, 1 : {1 : 1, 2 : 3, 3 : 4, 4 : 3}, 2 : {1 : 3, 2 : 1, 3 : 3, 4 : 4}, 3 : {1 : 4, 2 : 3, 3 : 1, 4 : 3}, 4 : {1 : 3, 2 : 4, 3 : 3, 4 : 1}}
left, right = 0, 0

move_case = {(left, right) : 0}
for number in line:
    next_case = {}
    for (left, right), weight in move_case.items():
        if left != number and ((left, number) not in next_case or next_case[(left, number)] > weight + move_weight[right][number]):
            next_case[(left, number)] = weight + move_weight[right][number]
        if number != right and ((number, right) not in next_case or next_case[(number, right)] > weight + move_weight[left][number]):
            next_case[(number, right)] = weight + move_weight[left][number]
    move_case = next_case
    
min_move = 1e9
for _, weight in move_case.items():
    if weight < min_move:
        min_move = weight
print(min_move) if min_move != 1e9 else print(0)