m, s = map(int, input().split())
if m == 1 and s == 0:
	print(0, 0)
elif s == 0 or 9 * m < s:
	print(-1, -1)
else:
	left = s -(m - 1) * 9
	if left > 0:
		low = f"{left}" + "9" * (m - 1)
		high = "9" * (m - 1) + f"{left}"
	else:
		count = (s - 1) // 9
		left = (s - 1) % 9
		low = "1" + "0" * (m - 2 - count) + f"{left}" + "9" * count
		
		count = s // 9
		left = s % 9
		high = "9" * count + f"{left}" + "0" * (m - count - 1)
	print(low, high)