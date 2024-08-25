class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        
        first = dummy
        second = dummy
        
        for _ in range(n):
            first = first.next
        
        while first.next:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next
    
# Approach:
# Two Pointers: We use two pointers, first and second. Initially, both pointers start at the head of the linked list.

# Move First Pointer: Move the first pointer n steps ahead of the second pointer.

# Move Both Pointers: After that, move both pointers one step at a time until the first pointer reaches the end of the list. At this point, the second pointer will be at the node just before the nth node from the end.

#Remove the nth Node: Adjust the next pointer of the second pointer to skip the nth node from the end.

Edge Case: If n is equal to the length of the list, the head of the list should be removed.