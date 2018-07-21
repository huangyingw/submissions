public class Solution
{
    public ListNode removeNthFromEnd(ListNode head, int n)
    {
        ListNode dummy = new ListNode(-1);
        dummy.next = head;
        ListNode quick = dummy, slow = dummy;

        for (int i = 0; i <= n; i++)
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
