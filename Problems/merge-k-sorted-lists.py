from heapq import heappop, heappush
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        
        for i, l in enumerate(lists):
            if l:  
                heappush(min_heap, (l.val, i, l))
        
        dummy = ListNode()
        current = dummy
        
        while min_heap:
            val, i, node = heappop(min_heap)
            current.next = node
            current = current.next
            if node.next:
                heappush(min_heap, (node.next.val, i, node.next))
        
        return dummy.next

# Approach:
# Min-Heap:

# Use a Min-Heap to keep track of the smallest node among all the heads of the linked lists.
# Insert the head of each non-empty linked list into the heap.
# Extract the smallest node from the heap, add it to the result linked list, and then push the next node from the same list into the heap.
# Repeat this process until all nodes from all lists have been added to the result list.
Time Complexity:

Building the heap initially takes 
𝑂
(
𝑘
log
⁡
𝑘
)
O(klogk), where 
𝑘
k is the number of linked lists.
Each extraction and insertion operation takes 
𝑂
(
log
⁡
𝑘
)
O(logk), and we perform this operation a total of 
𝑁
N times, where 
𝑁
N is the total number of nodes across all linked lists.
So, the total time complexity is 
𝑂
(
𝑁
log
⁡
𝑘
)
O(Nlogk), which is efficient for large inputs.