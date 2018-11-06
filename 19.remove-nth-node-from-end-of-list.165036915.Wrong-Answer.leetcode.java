public class Solution
{
    public ListNode removeNthFromEnd(ListNode head, int n)
    {
        if (head == null || head.next == null)
        {
            return null;
        }

        ListNode fast = head, slow = head;

        for (int i = 0; i <= n && fast != null; i++)
        {
            fast = fast.next;
        }


        while (fast != null)
        {
            slow = slow.next;
            fast = fast.next;
        }

        slow.next = slow.next.next;
        return head;
    }
}
