a, b, c = map(int, input().split())

s = set()
stack = [(0, 0, c)]
answer = set()
while stack:
    out = stack.pop()
    if out[0] == 0:
        answer.add(out[2])
    before = len(s)
    s.add(out)
    after = len(s)
    if before == after:
        continue
    else:
        if a != 0:
            ab = (out[1] + out[0] - min(b, out[1] + out[0]), min(b, out[1] + out[0]), out[2])
            ac = (out[2] + out[0] - min(c, out[2] + out[0]), out[1], min(c, out[2] + out[0]))
            stack.append(ab)
            stack.append(ac)
        if b != 0:
            ba = (min(a, out[1] + out[0]), out[0] + out[1] - min(a, out[1] + out[0]), out[2])
            bc = (out[0], out[1] + out[2] - min(c, out[2] + out[1]), min(c, out[2] + out[1]))
            stack.append(ba)
            stack.append(bc)
        if c != 0:
            ca = (min(a, out[2] + out[0]), out[1], out[2] + out[0] - min(a, out[2] + out[0]))
            cb = (out[0], min(b, out[2] + out[1]), out[1] + out[2] - min(b, out[2] + out[1]))
            stack.append(cb)
            stack.append(ca)

for num in sorted(answer):
    print(num, end = ' ')