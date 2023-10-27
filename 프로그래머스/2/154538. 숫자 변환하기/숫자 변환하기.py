def solution(x, y, n):
    case = [0] * (y + 1)
    case[x] = 1
    for idx in range(x, y):
        if case[idx] != 0:
            if idx + n <= y and (case[idx + n] == 0 or case[idx + n] > case[idx] + 1):
                case[idx + n] = case[idx] + 1
            if idx * 2 <= y and (case[idx * 2] == 0 or case[idx * 2] > case[idx] + 1):
                case[idx * 2] = case[idx] + 1
            if idx * 3 <= y and (case[idx * 3] == 0 or case[idx * 3] > case[idx] + 1):
                case[idx * 3] = case[idx] + 1
    return -1 if case[-1] == 0 else case[-1] - 1