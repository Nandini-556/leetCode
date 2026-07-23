# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        smaller_dummy = ListNode(0)
        greater_dummy = ListNode(0)

        smaller = smaller_dummy
        greater = greater_dummy

        while head:
            if head.val < x:
                smaller.next = head
                smaller = smaller.next
            else:
                greater.next = head
                greater = greater.next

            head = head.next

        greater.next = None
        smaller.next = greater_dummy.next

        return smaller_dummy.next