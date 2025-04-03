w, h, f, c, x1, y1, x2, y2 = map(int, input().split())

after_x = max(w - f, f)
after_y = h // (c + 1)
mul = c + 1

total = 0
total += mul * max(0, x2 - max(x1, min(f, w - f))) * (y2 - y1)
total += 2 * mul * (y2 - y1) * max(0, min(x2, min(f, w - f)) - x1)
print(w * h - total)