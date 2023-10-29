from collections import deque

def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sum_q1 = sum(queue1)
    sum_q2 = sum(queue2)
    target = (sum_q1 + sum_q2) / 2
    answer = 0
    
    while answer < len(queue1) * 2 + len(queue2) * 2:
        if sum_q1 > sum_q2:
            num = queue1.popleft()
            queue2.append(num)
            sum_q1 -= num
            sum_q2 += num
        elif sum_q1 == sum_q2:
            return answer
        else:
            num = queue2.popleft()
            queue1.append(num)
            sum_q2 -= num
            sum_q1 += num
        answer += 1
    
    return -1