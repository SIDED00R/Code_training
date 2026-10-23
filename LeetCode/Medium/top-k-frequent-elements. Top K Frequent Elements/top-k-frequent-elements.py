from collections import Counter
import heapq

class Solution:
	def topKFrequent(self, nums: list[int], k: int) -> list[int]:
		dic = Counter(nums)
		heap = []
		
		for key, value in dic.items():
			if len(heap) < k:
				heapq.heappush(heap, [value, key])
			else:
				front_value, front_key = heap[0]
				if front_value < value:
					heapq.heappop(heap)
					heapq.heappush(heap, [value, key])
		
		answer = []
		for now_case in heap:
			value, key = now_case
			answer.append(key)
		return answer