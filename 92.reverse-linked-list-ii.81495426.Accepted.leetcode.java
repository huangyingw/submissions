public class Solution
{
    public ListNode reverseBetween(ListNode head, int m, int n)
    {
        ListNode dummy = new ListNode(-1);
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
                ListNode temp = curr.next;
                curr.next = prev;
                prev = curr;
                curr = temp;
            }
        }

        prevM.next.next = curr;
        prevM.next = prev;
        return dummy.next;
    }
}
