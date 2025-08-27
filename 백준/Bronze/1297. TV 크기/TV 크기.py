d, h, w = map(int, input().split())

length = (h ** 2 + w ** 2)
mul = d ** 2 / length

print(int(mul ** 0.5 * h), int(mul ** 0.5 * w))
