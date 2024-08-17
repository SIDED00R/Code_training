def b_search(line, num):
    start = 0
    end = len(line) - 1
    while start <= end:
        mid = (start + end) // 2
        if line[mid] <= num:
            start = mid + 1
        else:
            end = mid - 1
    return start

n, q = map(int, input().split())
line = list(map(int, input().split()))
add_list = [0]
for num in line:
    add_list.append(num + add_list[-1])
    

for _ in range(q):
    l, r = map(int, input().split())
    s_idx = b_search(line, l)
    e_idx = b_search(line, r)
    if line[s_idx - 1] != l:
        s_idx += 1
    if e_idx - s_idx < 1:
        print(0)
    else:
        total_weight = add_list[e_idx] - add_list[s_idx - 1]
        middle = total_weight / (e_idx - s_idx + 1)
        m_idx = b_search(line, middle)
        if abs(line[m_idx] - middle) < abs(line[m_idx - 1] - middle):
            m_idx += 1
        min_value = (add_list[e_idx] - add_list[m_idx]) - line[m_idx - 1] * (e_idx - m_idx) + line[m_idx - 1] * (m_idx - s_idx) - (add_list[m_idx - 1] - add_list[s_idx - 1])
        max_value = max(add_list[e_idx] - add_list[s_idx] - line[s_idx - 1] * (e_idx - s_idx), line[e_idx - 1] * (e_idx - s_idx) - (add_list[e_idx - 1] - add_list[s_idx - 1]))
        print(max_value - min_value)
    