def find_largest_p(x):
    sign = 1
    if x < 0:
        sign = -1
        x = -x

    max_p = 1 
    for p in range(2, 32): 
        low, high = 2, int(x ** (1/p)) + 1

        while low <= high:
            mid = (low + high) // 2
            power = mid ** p

            if power == x:
                if sign == -1 and p % 2 == 0:
                    break 
                else:
                    max_p = p
                    break
            elif power < x:
                low = mid + 1
            else:
                high = mid - 1

    return max_p

while True:
    num = int(input())
    if num == 0:
        break
    print(find_largest_p(num))
