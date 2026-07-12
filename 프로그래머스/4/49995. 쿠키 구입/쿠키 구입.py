def solution(cookie):
    length = len(cookie)
    answer = 0
    for now in range(1, length):
        front_idx = now - 1
        back_idx = now
        front_sum = cookie[front_idx]
        back_sum = cookie[back_idx]
        while front_idx >= 0:
            try:
                if front_sum == back_sum:
                    answer = max(answer, front_sum)
                    front_idx -= 1
                    back_idx += 1
                    back_sum += cookie[back_idx]
                    front_sum += cookie[front_idx]
                elif front_sum > back_sum:
                    back_idx += 1
                    back_sum += cookie[back_idx]
                else:
                    front_idx -= 1
                    front_sum += cookie[front_idx]
            except:
                break
    return answer