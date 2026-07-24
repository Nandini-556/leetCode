"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None

        copied_nodes = {}

        current = head

        while current:
            copied_nodes[current] = Node(current.val)
            current = current.next

        current = head

        while current:
            copied_nodes[current].next = copied_nodes.get(current.next)
            copied_nodes[current].random = copied_nodes.get(current.random)
            current = current.next

        return copied_nodes[head]