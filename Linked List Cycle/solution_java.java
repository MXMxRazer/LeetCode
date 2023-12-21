/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {

        if (head == null) {
            return false;
        }

        ArrayList<ListNode> nodeList = new ArrayList<ListNode>();

        while(head.next != null) {
            head = head.next;
            nodeList.add(head);
            if (nodeList.contains(head.next)) {
                return true;
            }
        }
        return false;
    }
}
