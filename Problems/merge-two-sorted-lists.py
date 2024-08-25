# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        
        return dummy.next
    
# Approach:
# Create a Dummy Node: We initialize a dummy node that acts as the head of the merged list. A pointer current is used to build the merged list.

# Compare Nodes: Traverse both list1 and list2. At each step, compare the current nodes of both lists:

# Append the smaller node to the merged list.

# Move the pointer of the list whose node was appended.

# Attach Remaining Nodes: After the loop, if there are remaining nodes in either list1 or list2, append them directly to the merged list.

Return the Merged List: Finally, return the merged list, which starts from the node next to the dummy node.
