from collections import defaultdict, deque
import copy

class Solution:
	def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
		route = defaultdict(list)
		weight = {}
		for now_case in flights:
			fro, to, price = now_case
			route[fro].append(to)
			weight[(fro, to)] = price
			
		stack = [src]
		now_weight = {}
		now_weight[src] = 0
		next_weight_dic = copy.deepcopy(now_weight)
		
		for _ in range(k + 1):
			next_stack = []
			for now_node in stack:
				for next_node in route[now_node]:
					next_weight = now_weight[now_node] + weight[(now_node, next_node)]
					if next_node not in next_weight_dic:
						next_weight_dic[next_node] = next_weight
						next_stack.append(next_node)
					elif next_weight < next_weight_dic[next_node]:
						next_weight_dic[next_node] = next_weight
						next_stack.append(next_node)
			stack = next_stack[:]
			now_weight = copy.deepcopy(next_weight_dic)
		if dst in now_weight:
			return now_weight[dst]
		else:
			return -1