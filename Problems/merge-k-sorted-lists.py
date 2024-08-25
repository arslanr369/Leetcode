from heapq import heappop, heappush
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Min-Heap to keep track of the smallest elements
        min_heap = []
        
        # Initialize the heap with the head nodes of all the non-empty lists
        for i, l in enumerate(lists):
            if l:  # Check if the list is not empty
                heappush(min_heap, (l.val, i, l))
        
        # Dummy node to start the merged list
        dummy = ListNode()
        current = dummy
        
        # While there are nodes in the heap
        while min_heap:
            val, i, node = heappop(min_heap)
            # Add the smallest node to the merged list
            current.next = node
            current = current.next
            # If the node has a next, push it into the heap
            if node.next:
                heappush(min_heap, (node.next.val, i, node.next))
        
        return dummy.next
