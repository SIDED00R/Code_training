while True:
    try:
        l = list(map(float, input().split()))
        first = l[:2]
        second = l[2:4]
        third = l[4:6]
        forth = l[6:]
        total_list = [first, second, third, forth]
        left = []
        find = []
        for i in range(4):
            if find:
                if find != total_list[i]:
                    left += total_list[i]
                continue
            for j in range(i + 1, 4):
                if total_list[i] == total_list[j]:
                    find = total_list[i]
            if not find:
                left += total_list[i]

        mid_x = (left[0] + left[2]) / 2
        mid_y = (left[1] + left[3]) / 2
        print(format(mid_x * 2 - find[0], ".3f"), format(mid_y * 2 - find[1], ".3f"))
    except:
        break