import sys
sys.setrecursionlimit(10**6)

def go_down(nodes, now, array):
    if nodes[now][4] != "X":
        go_down(nodes, nodes[now][4], array)
    if nodes[now][5] != "X":
        go_down(nodes, nodes[now][5], array)
    array.append(nodes[now][3])
    

def solution(nodeinfo):
    N = len(nodeinfo)
    y_coordinate = [[] for _ in range(100001)]
    nodes = []
    height = 0
    for idx, node in enumerate(nodeinfo):
        x,y = node
        y_coordinate[y].append([x, idx + 1])
        if y > height:
            height = y
    y_coordinate = y_coordinate[:height + 1]
    start_idx = 0
    while y_coordinate:
        now_level = y_coordinate.pop()
        if now_level == []:
            continue
        now_level = sorted(now_level, key = lambda x: -x[0])
        now_nodes_N = len(now_level)        
        if nodes == []:
            #[left_bound, right_bound, x_coordinate, num, left_node, right_node]
            nodes.append([-1, 100001, now_level[0][0], now_level[0][1], "X", "X"])
        else:
            now_idx = start_idx
            while now_level:
                now_node = now_level.pop()
                change = False
                while not change:
                    left_bound, right_bound, x_coordinate, num = nodes[now_idx][:4]
                    if now_node[0] > left_bound and now_node[0] < x_coordinate:
                        nodes.append([left_bound, x_coordinate, now_node[0], now_node[1], "X", "X"])
                        nodes[now_idx][4] = len(nodes) - 1
                        change = True
                    elif now_node[0] > x_coordinate and now_node[0] < right_bound:
                        nodes.append([x_coordinate, right_bound, now_node[0], now_node[1], "X", "X"])
                        nodes[now_idx][5] = len(nodes) - 1
                        change = True
                    if not change:
                        now_idx += 1
        start_idx = len(nodes) - now_nodes_N
    
    stack = [nodes[0]]
    first = []
    second = []
    while stack:
        now = stack.pop()
        num, left_node, right_node = now[3:]
        first.append(num)
        if right_node != "X":
            stack.append(nodes[right_node])
        if left_node != "X":
            stack.append(nodes[left_node])
            
    go_down(nodes, 0, second)
        
    
    
    return [first,second]