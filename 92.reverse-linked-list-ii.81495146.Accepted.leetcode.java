public class Solution
{
    public ListNode reverseBetween(ListNode head, int m, int n)
    {
        ListNode dummy = new ListNode(-1);
        dummy.next = head;
        ListNode prevM = dummy;
        ListNode cur = null;
        ListNode prev = null;

        for (int i = 1; i <= n; i++)
        {
            if (i < m)
            {
                prevM = prevM.next;
            }
            else if (i == m)
            {
                prev = prevM.next;
                cur = prevM.next.next;
            }
            else
            {
                ListNode temp = cur.next;
                cur.next = prev;
                prev = cur;
                cur = temp;
            }
        }

        prevM.next.next = cur;
        prevM.next = prev;
        return dummy.next;
    }
}
