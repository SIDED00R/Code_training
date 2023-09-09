def isprime(p):
    for i in range(2, int(p ** 0.5) + 1):
        if p % i == 0:
            return False
    return True
        

    
def solution(nums):
    count = 0
    for fidx, f in enumerate(nums[:-2]):
        for sidx, s in enumerate(nums[fidx + 1:-1]):
            for tidx, t in enumerate(nums[sidx + fidx + 2:]):
                p = f + s + t
                if isprime(p):
                    print(f, s, t)
                    count += 1
        

    return count