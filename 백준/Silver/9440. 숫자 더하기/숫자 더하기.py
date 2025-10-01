while True:
    line = list(input().split())
    if line == ["0"]:
        break
    sort_line = sorted(line[1:])
    for idx, num in enumerate(sort_line):
        if num != "0":
            break
    f_f = sort_line[idx]
    s_f = sort_line[idx + 1]
    new_line = sort_line[:idx] + sort_line[idx + 2:]
    first = f_f + "".join(new_line[::2])
    second = s_f + "".join(new_line[1::2])
    print(int(first) + int(second))
        
       