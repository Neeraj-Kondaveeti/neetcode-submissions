"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        current = head
        hmap = {}

        while current:
            node = Node(x=current.val)
            hmap[current]= node
            current = current.next
        current = head
        while current:
            new_node = hmap[current]
            new_node.next = hmap[current.next] if current.next else None
            new_node.random = hmap[current.random] if current.random else None
            current = current.next
        return hmap[head]

