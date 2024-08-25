class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev_node = dummy
        
        while head and head.next:
            first_node = head
            second_node = head.next
            
            prev_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node
            
            prev_node = first_node
            head = first_node.next
            
        return dummy.next

# Approach:
# Iterative Solution:

# Use a dummy node to simplify edge cases, such as when the list has fewer than two nodes.
# Traverse the list two nodes at a time, swapping their pointers.
# Keep track of the previous node so that you can link it to the newly swapped pair.
# After swapping, move the pointer two nodes forward and repeat until the end of the list is reached or there is only one node left.
# Edge Cases:

# If the list is empty, return None.
# If the list has only one node, return the head as it is.