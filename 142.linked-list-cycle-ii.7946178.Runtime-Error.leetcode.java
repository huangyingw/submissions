public class Solution
{
    public ListNode detectCycle(ListNode head)
    {
        ListNode fast = head;
        ListNode slow = head;

        do
        {
            fast = fast.next.next;
            slow = slow.next;
        }
        while (fast != null && fast.next != null && fast != slow);

        if (fast == slow)
        {
            while (fast != null && fast != head)
            {
                fast = fast.next;
                head = head.next;
            }

            return fast;
        }

        return null;
    }
}

