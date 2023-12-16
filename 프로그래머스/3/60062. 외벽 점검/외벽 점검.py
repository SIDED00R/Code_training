from itertools import permutations

def solution(n, weak, dist):
    total_dist_case = list(permutations(dist, len(dist)))
    answer = n + 1

    for i in range(n):
        case = [n + num - i if num - i < 0 else num - i for num in weak]
        case = sorted(case, reverse = True)
        if case[-1] != 0:
            continue
        for dist_case in total_dist_case:
            count = 0
            test_case = case[:]
            for now_far in dist_case:
                start = test_case.pop()
                while test_case:
                    next_value = test_case[-1]
                    if next_value - start <= now_far:
                        test_case.pop()
                    else:
                        break
                count += 1
                if test_case == []:
                    break
            if answer > count and test_case == []:
                answer = count
    
    if answer == n + 1:
        return -1
    return answer