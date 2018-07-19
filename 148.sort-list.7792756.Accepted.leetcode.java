public class Solution
{

    private ListNode merge(ListNode h1, ListNode h2)
    {
        ListNode dummy = new ListNode(-1);

        for (ListNode p = dummy; h1 != null || h2 != null; p = p.next)
        {
            int val1 = h1 == null ? Integer.MAX_VALUE : h1.val;
            int val2 = h2 == null ? Integer.MAX_VALUE : h2.val;

            if (val1 <= val2)
            {
                p.next = h1;
                h1 = h1.next;
            }
            else
            {
                p.next = h2;
                h2 = h2.next;
            }
        }

        return dummy.next;
    }

    public ListNode sortList(ListNode head)
    {
        if (head == null || head.next == null)
        {
            return head;
        }

        ListNode fast = head, slow = head;

        while (fast.next != null && fast.next.next != null)
        {
            fast = fast.next.next;
            slow = slow.next;
        }

        fast = slow;
        slow = slow.next;
        fast.next = null;
        ListNode h1 = sortList(head);
        ListNode h2 = sortList(slow);
        return merge(h1, h2);
    }
}
