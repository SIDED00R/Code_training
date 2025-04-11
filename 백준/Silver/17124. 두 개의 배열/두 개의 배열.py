def find(l, num):
    first = 0
    end = len(l)
    if l[end - 1] < num:
        return end
    while first <= end:
        mid = (first + end) // 2
        if l[mid] > num:
            end = mid - 1
        else:
            first = mid + 1
    return first

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    n_list = list(map(int, input().split()))
    m_list = sorted(list(map(int, input().split())))
    answer = [0 for _ in range(len(n_list))]
    for i, num in enumerate(n_list):
        idx = find(m_list, num)
        if idx == 0:
            answer[i] = m_list[0]
        elif idx == len(m_list):
            answer[i] = m_list[-1]
        else:
            if abs(m_list[idx] - num) >= abs(m_list[idx - 1] - num):
                answer[i] = m_list[idx - 1]
            else:
                answer[i] = m_list[idx]
    print(sum(answer))
    
    
    