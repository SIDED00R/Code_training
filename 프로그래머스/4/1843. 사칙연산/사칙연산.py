from collections import defaultdict

def solution(arr):
    total_minus = []
    p_sum_minus = defaultdict(int)
    count = 0
    total = 0
    now_sign = 1
    for num in arr:
        if num.isnumeric():
            num = int(num)
            total += num
            if now_sign == -1:
                total_minus.append(num)
            p_sum_minus[count] += num
        elif num == "+":
            now_sign = 1
        else:
            now_sign = -1
            count += 1
    p_sum_minus[0] = 0
    answer = total - 2 * sum(total_minus)
    for idx in range(1, count + 1):
        answer = max(answer, total - 2 * (sum(total_minus[:idx - 1]) + p_sum_minus[idx]))
    return answer