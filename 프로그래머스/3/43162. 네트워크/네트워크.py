def solution(n, computers):
    connect = [0] * n
    counter = 0
    for idx in range(len(computers)):
        if connect[idx] == 0:
            counter += 1
            connect[idx] = counter
            stack = [computers[idx]]
            while stack != []:
                case = stack.pop()
                for i, con in enumerate(case):
                    if con == 1 and connect[i] == 0:
                        stack.append(computers[i])
                        connect[i] = counter
    return counter