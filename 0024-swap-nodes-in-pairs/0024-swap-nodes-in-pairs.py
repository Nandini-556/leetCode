# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head

        previous = dummy

        while previous.next and previous.next.next:
            first = previous.next
            second = first.next

            first.next = second.next
            second.next = first
            previous.next = second

            previous = first

        return dummy.next