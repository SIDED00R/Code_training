from itertools import combinations

class Solution:
	def readBinaryWatch(self, turnedOn: int) -> list[str]:
		m = [1, 2, 4, 8, 16, 32]
		h = [1, 2, 4, 8]
		
		answer = []
		for i in range(min(turnedOn + 1, 6)):
			left = turnedOn - i
			if left >= 4:
				continue
			for now_case in combinations(m, i):
				minute = sum(now_case)
				if minute >= 60:
					continue
				if left:
					for hour_case in combinations(h, left):
						hour = sum(hour_case)
						if hour >= 12:
							continue
						answer.append(f"{hour}:{minute:02d}")
				else:
					answer.append(f"{0}:{minute:02d}")
		return answer