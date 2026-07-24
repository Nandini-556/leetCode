# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        length = 0
        current = head

        while current:
            length += 1
            current = current.next

        part_size = length // k
        extra_nodes = length % k

        result = []
        current = head

        for index in range(k):
            part_head = current
            current_part_size = part_size

            if index < extra_nodes:
                current_part_size += 1

            for _ in range(current_part_size - 1):
                if current:
                    current = current.next

            if current:
                next_part = current.next
                current.next = None
                current = next_part

            result.append(part_head)

        return result