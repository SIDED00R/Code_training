from collections import defaultdict
import sys
sys.setrecursionlimit(10000000)

answer = 0
count = 0

def find(num, route, visited):
    global answer
    global count

    branches = [(0, 1)]                    # (깊이, 그 깊이의 노드 수). 자기 자신
    for next_node in route[num]:
        if not visited[next_node]:
            visited[next_node] = True
            next_depth, next_cnt = find(next_node, route, visited)
            branches.append((next_depth + 1, next_cnt))

    branches.sort(reverse=True)
    first_max = branches[0][0]
    second_max = branches[1][0] if len(branches) > 1 else -1

    if second_max >= 0:                    # 가지가 2개 이상일 때만 경로가 생김
        if first_max == second_max:        # 같은 깊이끼리 짝짓기
            s = sum(m for d, m in branches if d == first_max)
            sq = sum(m * m for d, m in branches if d == first_max)
            paths = (s * s - sq) // 2
        else:
            a = sum(m for d, m in branches if d == first_max)
            b = sum(m for d, m in branches if d == second_max)
            paths = a * b

        if answer < first_max + second_max:
            answer = first_max + second_max
            count = paths
        elif answer == first_max + second_max:
            count += paths

    return first_max, sum(m for d, m in branches if d == first_max)


def solution(n, edges):
    global answer
    global count
    answer = 0
    count = 0

    route = defaultdict(list)
    for edge in edges:
        a, b = edge
        route[a].append(b)
        route[b].append(a)

    visited = [False for _ in range(n + 1)]
    visited[1] = True
    find(1, route, visited)

    if count >= 2:
        return answer
    else:
        return answer - 1