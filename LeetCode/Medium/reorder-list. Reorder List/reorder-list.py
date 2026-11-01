# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def reorderList(self, head: ListNode | None) -> None:
		n = 0
		node = head
		while node:
			n += 1
			node = node.next

		front_len = (n + 1) // 2
		front_tail = head
		for _ in range(front_len - 1):
			front_tail = front_tail.next

		second_head = front_tail.next
		front_tail.next = None

		prev = None
		curr = second_head
		while curr:
			nxt = curr.next
			curr.next = prev
			prev = curr
			curr = nxt
		second_head = prev

		p1, p2 = head, second_head
		while p2:
			p1_next = p1.next
			p2_next = p2.next

			p1.next = p2
			if p1_next:
				p2.next = p1_next

			p1 = p1_next
			p2 = p2_next