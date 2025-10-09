from collections import defaultdict
from bisect import bisect_left

def div_num(num, count):
    diff = num - count
    count3 = diff // 2
    count2 = diff % 2
    count1 = count - count2 - count3
    return [3] * count3 + [2] * count2 + [1] * count1

def solution(edges, target):
    dic = defaultdict(list)
    for edge in edges:
        front, back = edge
        dic[front].append(back)
    
    now_tree = {}
    for k, v in dic.items():
        dic[k] = sorted(v)
        now_tree[k] = dic[k][0]
        
    answer = []
    for _ in range(10000):
        now_node = 1
        while True:
            next_node = now_tree[now_node]
            next_node_idx = bisect_left(dic[now_node], next_node)
            now_tree[now_node] = dic[now_node][(next_node_idx + 1) % len(dic[now_node])]
            if next_node not in now_tree:
                answer.append(next_node)
                break
            else:
                now_node = next_node
                
    check_list = []
    count = 0
    for num in target:
        if num > 0:
            count += 1
            check_list.append(False)
        else:
            check_list.append(True)
    
    answer_dic = {}
    for answer_idx in answer:
        idx = answer_idx - 1
        if idx not in answer_dic:
            answer_dic[idx] = [1, 3]
        else:
            min_count, max_count = answer_dic[idx]
            answer_dic[idx] = [min_count + 1, max_count + 3]
            
        check = False
        if answer_dic[idx][0] <= target[idx] <= answer_dic[idx][1]:
            check = True
        
        if check:
            if check_list[idx] == False:
                check_list[idx] = True
                count -= 1
        else:
            if check_list[idx] == True:
                return[-1]
            
        if count == 0:
            break
    
    able_list = {}
    for k, v in answer_dic.items():
        num = target[k]
        count = v[0]
        out_list = div_num(num, count)
        able_list[k + 1] = out_list
        
    result = []
    print(answer[:12])
    print(able_list)
    try:
        for answer_idx in answer:
            out = able_list[answer_idx].pop()
            result.append(out)
    except:
        print(able_list)
        return result
    
    return 1