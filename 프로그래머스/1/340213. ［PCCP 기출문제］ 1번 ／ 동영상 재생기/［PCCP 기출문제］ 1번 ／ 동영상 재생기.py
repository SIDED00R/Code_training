def solution(video_len, pos, op_start, op_end, commands):
    vm, vs = map(int, video_len.split(":"))
    pm, ps = map(int, pos.split(":"))
    osm, oss = map(int, op_start.split(":"))
    oem, oes = map(int, op_end.split(":"))
    v = vm * 60 + vs
    p = pm * 60 + ps
    os = osm * 60 + oss
    oe = oem * 60 + oes
    
    for c in commands:
        if os <= p <= oe:
            p = oe
        if c == "next":
            if os <= p + 10 <= oe:
                p = oe
            else:
                p += 10
                p = min(v, p)
        else:
            if os <= p - 10 <= oe:
                p = oe
            else:
                p -= 10
                p = max(0, p)
                
    a_m = str(p // 60).zfill(2)
    a_s = str(p % 60).zfill(2)
                
    return f"{a_m}:{a_s}"