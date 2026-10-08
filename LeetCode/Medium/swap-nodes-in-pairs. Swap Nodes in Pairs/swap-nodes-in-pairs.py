# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def swapPairs(self, head: ListNode | None) -> ListNode | None:
		stack = []
		answer = ListNode()
		tail = answer
		while True:
			if head is None:
				while stack:
					out = stack.pop()
					tail.next = ListNode(out)
					tail = tail.next
				return answer.next
			now = head.val
			stack.append(now)
			if len(stack) == 2:
				while stack:
					out = stack.pop()
					tail.next = ListNode(out)
					tail = tail.next
			head = head.next