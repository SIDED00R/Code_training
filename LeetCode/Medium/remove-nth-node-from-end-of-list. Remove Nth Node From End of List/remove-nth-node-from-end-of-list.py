# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
		dummy = ListNode(0, head)
		
		def check(node):
			if node is None:
				return 0
			count = check(node.next) + 1
			if count == n + 1:
				node.next = node.next.next
			return count
		
		check(dummy)
		return dummy.next