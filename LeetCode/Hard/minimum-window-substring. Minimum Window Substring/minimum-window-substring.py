from collections import deque, Counter

class Solution:
	def minWindow(self, s: str, t: str) -> str:
		answer = 1000001
		ans_str = ""
		check = Counter(t)
		counter = len(check)
		
		q = deque()
		for alp in s:
			q.append(alp)
			if alp in check:
				check[alp] -= 1
				if check[alp] == 0:
					counter -= 1
					while counter == 0:
						out = q.popleft()
						if out in check:
							check[out] += 1
							if check[out] > 0:
								if answer > len(q) + 1:
									answer = len(q) + 1
									ans_str = out + "".join(q)
								counter += 1
			
		return ans_str