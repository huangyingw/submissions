public class Solution
{
    public ListNode deleteDuplicates(ListNode head)
    {
        if (head == null || head.next == null)
        {
            return head;
        }

        for (ListNode current = head; current.next != null; current = current.next)
        {
            ListNode next = current.next;

            while (next != null && next.val == current.val)
            {
                next = next.next;
            }

            current.next = next;
        }

        return head;
    }
}

