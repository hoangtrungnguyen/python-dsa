# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order, and each of their nodes contains a
# single digit. Add the two numbers and return the sum as a linked list.
#
#  You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
#
#
#  Example 1:
#
#
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
#
#
#  Example 2:
#
#
# Input: l1 = [0], l2 = [0]
# Output: [0]
#
#
#  Example 3:
#
#
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
#
#
#
#  Constraints:
#
#
#  The number of nodes in each linked list is in the range [1, 100].
#  0 <= Node.val <= 9
#  It is guaranteed that the list represents a number that does not have
# leading zeros.
#
#
from optparse import Option
from typing import List
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        """
        Returns a string representation of the linked list.  

        """
        result = ""
        current = self
        while current:
            result += str(current.val)
            if current.next:
                result += " -> "
            current = current.next
        return f'{result} -> None'



class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
       #  each level
       #    add the number from both list together then get the remainder.
       # remain = -1
       # while l1 is not None and l2 is not None:
       return self.action(l1, l2, 0)

    def action(self, l1: Optional[ListNode], l2: Optional[ListNode], carry: int) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            if carry == 0:
                return None
            return ListNode(carry)

        if l1 is not None and l2 is not None:
            total = l1.val + l2.val + carry
            carry = total // 10
            digit = total % 10
            return ListNode(digit , self.action(l1.next, l2.next, carry))

        if l1 is not None:
            total = l1.val + carry
            carry = total // 10
            digit = total % 10
            return ListNode(digit, self.action(l1.next, l2, carry))

        if l2 is not None:
            total = l2.val + carry
            carry = total // 10
            digit = total % 10
            return ListNode(digit, self.action(l1, l2.next, carry))

n1 = ListNode(2, ListNode(4, ListNode(3, )))
n2 = ListNode(5, ListNode(6, ListNode(4, )))
r = Solution().addTwoNumbers(n1, n2)
print(r)
n1 = ListNode(9, ListNode(9, ))
n2 = ListNode(1, )
r = Solution().addTwoNumbers(n1, n2)
print(r)
n1 = ListNode(0)
n2 = ListNode(0)
r = Solution().addTwoNumbers(n1, n2)
print(r)
n1 = ListNode(9, ListNode(9, ListNode(9, )))
n2 = ListNode(1, )
r = Solution().addTwoNumbers(n1, n2)
print(r)









