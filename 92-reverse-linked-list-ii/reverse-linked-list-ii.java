/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseBetween(ListNode head, int left, int right) {
        int index = 0;
        if(head == null || left == right){
            return head;
        }

        ListNode dummy = new ListNode(0, head);
        ListNode prevLeftNode = dummy;

        for(int i = 0; i < left - 1; i ++){
            if (prevLeftNode == null) { // Should not happen given constraints 1 <= left <= n
                return head; // Or throw an error
            }
            prevLeftNode = prevLeftNode.next;
        }

        // tail of sublist is going to be head of reversed segmented list
        ListNode tailOfReversedSublist = prevLeftNode.next;

        if (tailOfReversedSublist == null) {
             return dummy.next; // Or head
        }

        ListNode prevNodeReversedSublist = null;
        ListNode currentNodeToProcess = tailOfReversedSublist;
        for(int i = 0; i < right - left + 1; i ++) {
            if(currentNodeToProcess == null){
                break;
            }
            ListNode nextNode = currentNodeToProcess.next;
            currentNodeToProcess.next = prevNodeReversedSublist;
            prevNodeReversedSublist = currentNodeToProcess;
            currentNodeToProcess = nextNode;
        }

        prevLeftNode.next = prevNodeReversedSublist;
        if(tailOfReversedSublist != null){
            tailOfReversedSublist.next = currentNodeToProcess;
        }
        return dummy.next;
    }
}