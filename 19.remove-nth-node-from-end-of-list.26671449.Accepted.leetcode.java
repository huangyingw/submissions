/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution
{
    public ListNode removeNthFromEnd(ListNode head, int n)
    {
        if (head == null || head.next == null)
        {
            return null;
        }

        ListNode dummy = new ListNode(-1);
        dummy.next = head;
        ListNode quick = dummy, slow = dummy;

        for (int i = 0; i <= n && quick != null; i++)
        {
            quick = quick.next;
        }

        while (quick != null)
        {
            slow = slow.next;
            quick = quick.next;
        }

        slow.next = slow.next.next;
        return dummy.next;
    }
}
