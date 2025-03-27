def check(diff, time, level, before_time):
    if diff <= level:
        return time
    else:
        return (time + before_time) * (diff - level) + time

def solution(diffs, times, limit):
    front = 1
    end = 100000
    while front <= end:
        mid = (front + end) // 2
        total = times[0]
        for idx in range(1, len(diffs)):
            total += check(diffs[idx], times[idx], mid, times[idx - 1])
        if total > limit:
            front = mid + 1
        else:
            end = mid - 1

    return front