import copy

def finish_early(board, me, you, count):
    count += 1
    n = len(board)
    m = len(board[0])
    di = [0, -1, 0, 1]
    dj = [1, 0, -1, 0]
    i_always_win = False
    short = []
    long = [count - 1]
    for idx in range(4):
        if (0 <= me[0] + di[idx] < n) and (0 <= me[1] + dj[idx] < m) and board[me[0] + di[idx]][me[1] + dj[idx]] != 0:
            if me == you:
                return [True, count]
            new_board = copy.deepcopy(board)
            new_board[me[0]][me[1]] = 0
            you_win = finish_early(new_board, you, [me[0] + di[idx], me[1] + dj[idx]], count)
            if not you_win[0]:
                i_always_win = True
                short.append(you_win[1])
            else:
                long.append(you_win[1])
    if i_always_win:
        return [True, min(short)]
    else:
        return [False, max(long)]

def solution(board, aloc, bloc):
    answer = finish_early(board, aloc, bloc, 0)
    return answer[1]