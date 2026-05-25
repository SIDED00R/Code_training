n = int(input())
n_list = sorted(map(int, input().split()))
m = int(input())
m_list = sorted(map(int, input().split()))

n_idx = 0
m_idx = 0
answer = 0
while n_idx < n and m_idx < m:
    if abs(n_list[n_idx] - m_list[m_idx]) <= 1:
        answer += 1
        n_idx += 1
        m_idx += 1
    else:
        if n_list[n_idx] < m_list[m_idx]:
            n_idx += 1
        else:
            m_idx += 1
            
print(answer)