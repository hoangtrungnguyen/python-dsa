# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        node_hash_map = dict()
        curr_A = headA
        while curr_A is not None:
            node_hash_map[curr_A] = 1
            curr_A = curr_A.next
        
        curr_B = headB
        while curr_B is not None:
            if curr_B in node_hash_map:
                return curr_B
            curr_B = curr_B.next
        return None