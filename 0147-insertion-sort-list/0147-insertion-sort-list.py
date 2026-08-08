class Solution:
    def insertionSortList(self, head):
        dummy = ListNode(0)
        curr = head

        while curr:
            # Save the next node
            next_node = curr.next

            # Find where curr should be inserted
            prev = dummy

            while prev.next and prev.next.val < curr.val:
                prev = prev.next

            # Insert curr
            curr.next = prev.next
            prev.next = curr

            # Move to the next unsorted node
            curr = next_node

        return dummy.next