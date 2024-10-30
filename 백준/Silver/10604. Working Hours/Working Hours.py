def add_time():
    hh, mm = 0, 0
    for t in total_time:
        if ":" in t:
            h, m = t[1:].split(":")
        else:
            h, m = t[1:].split(".")
        if h == "":
            h = 0
        if m == "":
            m = 0
        if t[0] == "+":
            hh += int(h)
            mm += int(m)
        else:
            hh -= int(h)
            mm -= int(m)
    total = hh * 60 + mm
    return total // 60, total % 60

total_time = []
while True:
    time = input()
    if time == "$$$":
        h, m = add_time()
        m = format(m, '02')
        print(f"{h}:{m}")
        total_time = []
    elif time == "###":
        h, m = add_time()
        m = format(m, '02')
        print(f"{h}:{m}")
        break
    else:
        total_time.append(time)