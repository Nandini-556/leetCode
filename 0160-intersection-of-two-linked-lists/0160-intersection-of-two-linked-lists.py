# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        pointer_a = headA
        pointer_b = headB

        while pointer_a != pointer_b:
            if pointer_a:
                pointer_a = pointer_a.next
            else:
                pointer_a = headB

            if pointer_b:
                pointer_b = pointer_b.next
            else:
                pointer_b = headA

        return pointer_a