class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # Dummy node to help with edge cases
        dummy = ListNode(0)
        dummy.next = head
        prev_group = dummy
        
        while True:
            # Check if there are at least k nodes left to reverse
            kth_node = self.get_kth_node(prev_group, k)
            if not kth_node:
                break
            
            # Reverse the k nodes
            next_group = kth_node.next
            prev, curr = kth_node.next, prev_group.next
            
            # Reverse the current group
            while curr != next_group:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            # Connect with the previous part of the list
            temp = prev_group.next
            prev_group.next = kth_node
            prev_group = temp
        
        return dummy.next
    
    def get_kth_node(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
