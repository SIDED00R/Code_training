def popcount(n):
    return bin(n).count('1')

def charging_chaos(idx, n, l):

    o_datas = list(input().split())
    outlets = set(int(data, 2) for data in o_datas)
    d_datas = list(input().split())
    devices = set(int(data, 2) for data in d_datas)
    min_flips = float('inf')
    
    for outlet in outlets:
        flip_pattern = next(iter(devices)) ^ outlet
        flipped_outlets = {o ^ flip_pattern for o in outlets}
        if flipped_outlets == devices:
            min_flips = min(min_flips, popcount(flip_pattern))
    
    if min_flips == float('inf'):
        result = f"Case #{idx + 1}: NOT POSSIBLE"
    else:
        result = f"Case #{idx + 1}: {min_flips}"
    results.append(result)
    
    
results = []
for idx in range(int(input())):
    n, l = map(int, input().split())
    charging_chaos(idx, n, l)

for result in results:
    print(result)