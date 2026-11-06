import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
		heap = []
		for idx in range(len(lists)):
			if lists[idx] is not None:
				heapq.heappush(heap, [lists[idx].val, idx])
		answer = ListNode()
		answer_pointer = answer
		while heap:
			value, idx = heapq.heappop(heap)
			now_node = ListNode(value)
			answer_pointer.next = now_node
			answer_pointer = answer_pointer.next
			if lists[idx].next is not None:
				lists[idx] = lists[idx].next
				heapq.heappush(heap, [lists[idx].val, idx])
		return answer.next