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
    
#