from typing import Optional
from typing import List

# Definition fo\r singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def create_linked_list(arr: List[int]) -> Optional[ListNode]:
    """
    Creates a linked list from a given array of integers.

    Args:
      arr: The array of integers to convert to a linked list.

    Returns:
      The head of the created linked list, or None if the array is empty.
    """
    if not arr:
        return None

    head = ListNode(arr[0])  # Create the head node
    current = head
    for val in arr[1:]:  # Iterate through the rest of the array
        current.next = ListNode(val)  # Create a new node and link it
        current = current.next  # Move to the newly created node

    return head