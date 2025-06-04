# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head is None:
            return None
        dummy = ListNode(0, head)
        prev_left_node = dummy

        for _ in range(left - 1):
            prev_left_node = prev_left_node.next

        tail_of_sublist = prev_left_node.next
        prev_node = None
        current = tail_of_sublist # Start iterating from the left-th node.

        for _ in range(right - left + 1):
            next_node = current.next
            current.next = prev_node
            prev_node = current
            current = next_node

        prev_left_node.next = prev_node
        tail_of_sublist.next = current

        return dummy.next
