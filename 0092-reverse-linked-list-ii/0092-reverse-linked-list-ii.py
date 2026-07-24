# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head

        previous = dummy

        for _ in range(left - 1):
            previous = previous.next

        current = previous.next

        for _ in range(right - left):
            next_node = current.next
            current.next = next_node.next
            next_node.next = previous.next
            previous.next = next_node

        return dummy.next