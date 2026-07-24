# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        slow = head
        fast = head
        previous = None

        while fast and fast.next:
            previous = slow
            slow = slow.next
            fast = fast.next.next

        previous.next = None

        left = self.sortList(head)
        right = self.sortList(slow)

        return self.merge(left, right)

    def merge(self, first, second):
        dummy = ListNode(0)
        tail = dummy

        while first and second:
            if first.val <= second.val:
                tail.next = first
                first = first.next
            else:
                tail.next = second
                second = second.next

            tail = tail.next

        if first:
            tail.next = first
        else:
            tail.next = second

        return dummy.next