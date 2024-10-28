from typing import Optional

from linked_list_utilities.utilities import ListNode
from linked_list_utilities.utilities import create_linked_list


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        hasCycle = False
        while fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                hasCycle = True
                break
        return hasCycle



print(Solution().hasCycle(create_linked_list([3,2,0,-4])))