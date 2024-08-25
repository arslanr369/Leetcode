class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        prev_group = dummy
        
        while True:
            kth_node = self.get_kth_node(prev_group, k)
            if not kth_node:
                break
            
            next_group = kth_node.next
            prev, curr = kth_node.next, prev_group.next
            
            while curr != next_group:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            temp = prev_group.next
            prev_group.next = kth_node
            prev_group = temp
        
        return dummy.next
    
    def get_kth_node(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

# Approach:
# Iterative Reversal of Groups:

# We will reverse the nodes in groups of k until we reach the end of the list.
# If the remaining nodes are fewer than k, they will not be reversed.
# Use a dummy node to handle the head of the list and make it easier to manipulate the linked list.
# Key Steps:

# Traverse the list and check if there are enough nodes left for a full group of k.
# Reverse the k nodes.
# Connect the reversed segment to the previous and next parts of the list.
# Move to the next group.
# Edge Cases:

# If k is 1, return the list as it is because no reversing is needed.
# If the list has fewer than k nodes, return the list as it is.