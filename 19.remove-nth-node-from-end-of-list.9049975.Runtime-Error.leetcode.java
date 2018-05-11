public class Solution
{
    public ListNode removeNthFromEnd(ListNode head, int n)
    {
        ListNode fast = head;

        while (n > 0 && fast != null)
        {
            fast = fast.next;
            n--;
        }

        if (n > 0 && fast == null)
        {
            return head.next;
        }

        ListNode slow = head;

        while (fast != null)
        {
            slow = slow.next;
            fast = fast.next;
        }

        slow.next = slow.next.next;
        return head;
    }
}
