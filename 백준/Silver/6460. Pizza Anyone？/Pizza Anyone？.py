import sys
input = sys.stdin.readline

dic = {chr(i): i - ord('A') for i in range(ord('A'), ord('P') + 1)} 
while True:
    l = []
    line = input()
    if not line:
        break
    line = line.strip()

    while line != ".":
        l.append(line[:-1]) 
        line = input()
        if not line:
            break
        line = line.strip()

    if not line:
        break

    found = False
    for mask in range(1 << 16):
        ok = True
        for s in l:
            sat = False
            for i in range(0, len(s), 2):
                sign = s[i]
                ch = s[i+1]
                idx = dic[ch]
                bit = (mask >> idx) & 1
                if (sign == '+' and bit == 1) or (sign == '-' and bit == 0):
                    sat = True
                    break
            if not sat:
                ok = False
                break

        if ok:
            topping = ''.join(chr(ord('A') + i) for i in range(16) if (mask >> i) & 1)
            print("Toppings: " + topping)
            found = True
            break

    if not found:
        print("No pizza can satisfy these requests.")
