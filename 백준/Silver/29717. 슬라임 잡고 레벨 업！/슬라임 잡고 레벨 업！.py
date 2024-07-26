for _ in range(int(input())):
    n = int(input())
    total_exp = n * (n + 1) // 2
    min_level = 1
    max_level = int(1e10)
    while min_level <= max_level:
        level = (min_level + max_level) // 2
        if level * (level + 1) <= total_exp:
            min_level = level + 1
        else:
            max_level = level - 1
    print(min_level)

