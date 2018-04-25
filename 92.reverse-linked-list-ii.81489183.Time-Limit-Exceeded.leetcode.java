public class Solution
{
    public ListNode reverseBetween(ListNode head, int m, int n)
    {
        ListNode dummy = new ListNode(-1);
        dummy.next = head;
        ListNode prevM = dummy;
        ListNode curr = null;
        ListNode temp = null;

        for (int i = 1; i <= n; i++)
        {
            if (i < m)
            {
                prevM = prevM.next;
            }
            else if (i == m)
            {
                curr = prevM.next.next;
            }
            else
            {
                temp = curr.next;
                curr.next = prevM.next;
                prevM = curr;
                curr = temp;
            }
        }

        return dummy.next;
    }
}
