/**
 * Example:
 * var li = ListNode(5)
 * var v = li.`val`
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 */
class Solution {
    fun reverseBetween(head: ListNode?, left: Int, right: Int): ListNode? {
        if (head == null || left == right) {
            return head // No operation needed for empty list or when left equals right
        }

        // Create a sentinel node to handle cases where reversal starts from the head (left = 1)
        val sentinel = ListNode(0) // The value of the sentinel node doesn't matter
        sentinel.next = head
        
        // 1. Navigate to the node just before the sublist to be reversed
        //    This node will be `prevLeftNode`.
        var prevLeftNode: ListNode? = sentinel
        for (i in 0 until left - 1) { // Loop (left - 1) times
            prevLeftNode = prevLeftNode?.next
            // This check is for extreme edge cases or invalid inputs,
            // though problem constraints (1 <= left <= n) usually prevent prevLeftNode from becoming null here.
            if (prevLeftNode == null) {
                return head // Or sentinel.next, effectively the original list
            }
        }

        // `prevLeftNode` is now positioned at the (left-1)th node.
        // `prevLeftNode.next` is the first node of the sublist to reverse (the `left`-th node).
        // This first node of the sublist will become the tail of the reversed segment.
        val firstNodeOfSublist: ListNode? = prevLeftNode?.next 
        
        // If `firstNodeOfSublist` is null, it implies `left` is out of bounds for the list's length.
        // (e.g. list has 3 nodes, left = 4). Constraints usually prevent this.
        if (firstNodeOfSublist == null) {
            return sentinel.next // Original list
        }

        // 2. Reverse the sublist from the `left`-th node to the `right`-th node
        var prevNodeInReversal: ListNode? = null
        var currentNodeToProcess: ListNode? = firstNodeOfSublist
        
        for (i in 0 until (right - left + 1)) { // Loop (right - left + 1) times, which is the length of the sublist
            if (currentNodeToProcess == null) {
                // This break handles cases where `right` might be out of bounds,
                // though problem constraints (right <= n) usually prevent this.
                break
            }
            val nextNodeTemp: ListNode? = currentNodeToProcess.next // Store the next node
            currentNodeToProcess.next = prevNodeInReversal         // Reverse the current node's pointer
            prevNodeInReversal = currentNodeToProcess              // Move prevNodeInReversal one step forward
            currentNodeToProcess = nextNodeTemp                    // Move currentNodeToProcess one step forward
        }

        // After the reversal loop:
        // - `prevNodeInReversal` points to the new head of the reversed sublist (originally the `right`-th node).
        // - `currentNodeToProcess` points to the node that was originally after the `right`-th node.
        // - `firstNodeOfSublist` (which was the original `left`-th node) is now the tail of the reversed segment.
        //   Its `next` pointer is currently pointing to the node before it in the reversed sequence (or null if it was the last).

        // 3. Connect the reversed sublist back into the main list
        prevLeftNode?.next = prevNodeInReversal // Connect [node before sublist] -> [new head of reversed sublist]
        
        // `firstNodeOfSublist` is guaranteed not to be null here due to the earlier check.
        firstNodeOfSublist.next = currentNodeToProcess // Connect [tail of reversed sublist] -> [node after original sublist]

        // 4. Return the head of the modified list (which is sentinel.next)
        return sentinel.next
    }
}