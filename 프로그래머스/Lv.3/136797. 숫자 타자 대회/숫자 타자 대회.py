def solution(numbers):
    move_weight = {0 : {0 : 1, 1 : 7, 2 : 6, 3 : 7, 4 : 5, 5 : 4, 6 : 5, 7 : 3, 8 : 2, 9 : 3},
                   1 : {0 : 7, 1 : 1, 2 : 2, 3 : 4, 4 : 2, 5 : 3, 6 : 5, 7 : 4, 8 : 5, 9 : 6},
                   2 : {0 : 6, 1 : 2, 2 : 1, 3 : 2, 4 : 3, 5 : 2, 6 : 3, 7 : 5, 8 : 4, 9 : 5},
                   3 : {0 : 7, 1 : 4, 2 : 2, 3 : 1, 4 : 5, 5 : 3, 6 : 2, 7 : 6, 8 : 5, 9 : 4},
                   4 : {0 : 5, 1 : 2, 2 : 3, 3 : 5, 4 : 1, 5 : 2, 6 : 4, 7 : 2, 8 : 3, 9 : 5},
                   5 : {0 : 4, 1 : 3, 2 : 2, 3 : 3, 4 : 2, 5 : 1, 6 : 2, 7 : 3, 8 : 2, 9 : 3},
                   6 : {0 : 5, 1 : 5, 2 : 3, 3 : 2, 4 : 4, 5 : 2, 6 : 1, 7 : 5, 8 : 3, 9 : 2},
                   7 : {0 : 3, 1 : 4, 2 : 5, 3 : 6, 4 : 2, 5 : 3, 6 : 5, 7 : 1, 8 : 2, 9 : 4},
                   8 : {0 : 2, 1 : 5, 2 : 4, 3 : 5, 4 : 3, 5 : 2, 6 : 3, 7 : 2, 8 : 1, 9 : 2},
                   9 : {0 : 3, 1 : 6, 2 : 5, 3 : 4, 4 : 5, 5 : 3, 6 : 2, 7 : 4, 8 : 2, 9 : 1}}
    left, right = 4, 6
    move_case = {(left, right) : 0}
    for number in numbers:
        next_case = {}
        now = int(number)
        for (left, right), weight in move_case.items():
            if left != now and ((left, now) not in next_case or next_case[(left, now)] > weight + move_weight[right][now]):
                next_case[(left, now)] = weight + move_weight[right][now]
            if now != right and ((now, right) not in next_case or next_case[(now, right)] > weight + move_weight[left][now]):
                next_case[(now, right)] = weight + move_weight[left][now]
        move_case = next_case
        
    min_move = 1e9
    for _, weight in move_case.items():
        if weight < min_move:
            min_move = weight
    return min_move