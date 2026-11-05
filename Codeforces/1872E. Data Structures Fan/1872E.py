import sys

def main():
	data = sys.stdin.buffer.read().split()
	idx = 0
	t = int(data[idx]); idx += 1
	out = []

	for _ in range(t):
		n = int(data[idx]); idx += 1
		a = data[idx:idx+n]
		a = list(map(int, a)); idx += n
		s = data[idx].decode(); idx += 1
		q = int(data[idx]); idx += 1

		# prefix xor: prefix[i] = a_1 ^ ... ^ a_i (1-indexed), prefix[0]=0
		prefix = [0] * (n + 1)
		for i in range(1, n + 1):
			prefix[i] = prefix[i - 1] ^ a[i - 1]

		X = prefix[n]  # 전체 XOR

		# 초기 ans1: s_i == '1' 인 인덱스들의 a XOR
		ans1 = 0
		for i in range(n):
			if s[i] == '1':
				ans1 ^= a[i]

		res = []
		for _ in range(q):
			tp = int(data[idx]); idx += 1
			if tp == 1:
				l = int(data[idx]); r = int(data[idx+1]); idx += 2
				ans1 ^= prefix[r] ^ prefix[l - 1]
			else:
				g = int(data[idx]); idx += 1
				if g == 1:
					res.append(ans1)
				else:
					res.append(X ^ ans1)

		out.append(' '.join(map(str, res)))

	print('\n'.join(out))

main()