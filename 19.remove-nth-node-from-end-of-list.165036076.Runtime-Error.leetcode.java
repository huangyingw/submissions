public class Solution
{
    public ListNode removeNthFromEnd(ListNode head, int n)
    {
        ListNode fast = head;
        ListNode slow = head;

        for (int i = 0; i <= n; i++)
        {
            fast = fast.next;
        }

        while (fast != null)
        {
            fast = fast.next;
            slow = slow.next;
        }

        slow.next = slow.next.next;
        return head;
    }
}