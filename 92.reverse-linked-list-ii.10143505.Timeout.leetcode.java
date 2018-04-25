public class Solution
{
    public ListNode reverseBetween(ListNode head, int m, int n)
    {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prevM = dummy;
        ListNode prev = null;
        ListNode curr = null;

        for (int i = 1; i <= n; i++)
        {
            if (i < m)
            {
                prevM = prevM.next;
            }
            else if (i == m)
            {
                prev = prevM.next;
                curr = prevM.next.next;
            }
            else
            {
                prevM.next.next = curr.next;
                curr.next = prevM.next;
                prevM.next = curr;
                curr = prev.next;
            }
        }

        return dummy.next;
    }
}

