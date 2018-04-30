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
    public ListNode deleteDuplicates(ListNode head)
    {
        if (head == null)
        {
            return head;
        }

        for (ListNode cur = head; cur != null; cur = cur.next)
        {
            ListNode next = cur.next;

            while (next != null && next.val == cur.val)
            {
                next = next.next;
            }

            cur.next = next;
        }

        return head;
    }
}
