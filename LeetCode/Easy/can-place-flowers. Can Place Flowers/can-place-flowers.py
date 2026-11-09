class Solution:
	def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
		
		length = len(flowerbed)
		answer = 0
		if length == 1:
			if flowerbed[0] == 0:
				answer += 1
		else:
			if flowerbed[0] == 0 and flowerbed[1] == 0:
				answer += 1
				flowerbed[0] = 1
			if flowerbed[-1] == 0 and flowerbed[-2] == 0:
				answer += 1
				flowerbed[-1] = 1
		
		for i in range(1, length - 1):
			if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0 and flowerbed[i] == 0:
				answer += 1
				flowerbed[i] = 1
		return answer >= n