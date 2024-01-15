from collections import defaultdict

def find_shape(board, N, simbol, case, now):
    di = [0, -1, 0, 1]
    dj = [1, 0, -1, 0]
    stack = [now]
    board[now[0]][now[1]] = 1 - simbol    
    move = []
    while stack:
        i, j = stack.pop()
        move.append([i - now[0], j - now[1]])
        for idx in range(4):
            if 0 <= i + di[idx] < N and 0 <= j + dj[idx] < N and board[i + di[idx]][j + dj[idx]] == simbol:
                stack.append([i + di[idx], j + dj[idx]])
                board[i + di[idx]][j + dj[idx]] = 1 - simbol    
    case.append(move)
    return

def make_piece(cases, pieces):
    for case in cases:
        N = len(case)
        min_i, min_j, max_i, max_j = 0, 0, 0, 0
        for block in case:
            block_i, block_j = block
            if block_i > max_i:
                max_i = block_i
            if block_j < min_j:
                min_j = block_j
            if block_j > max_j:
                max_j = block_j
        max_j -= min_j
        piece = [[0 for _ in range(max_j + 1)] for _ in range(max_i + 1)]
        for block in case:
            piece[block[0]][block[1] - min_j] = 1
        pieces[N].append(piece)
    return 

def rotate_piece(piece):
    new_piece= list(map(list, zip(*piece[::-1])))
    return new_piece


def solution(game_board, table):
    N = len(game_board)
    game_board_cases = []
    tabel_cases = []
    for i in range(N):
        for j in range(N):
            if game_board[i][j] == 0:
                find_shape(game_board, N, 0, game_board_cases, [i, j])
            if table[i][j] == 1:
                 find_shape(table, N, 1, tabel_cases, [i, j])
    
    game_board_pieces = defaultdict(list)
    table_pieces = defaultdict(list)
    make_piece(game_board_cases, game_board_pieces)
    make_piece(tabel_cases, table_pieces)
    
    answer = 0
    for key, values in game_board_pieces.items():
        for value in values:
            for _ in range(4):
                value = rotate_piece(value)
                if value in table_pieces[key]:
                    answer += key
                    table_pieces[key].remove(value)
                    break

    return answer